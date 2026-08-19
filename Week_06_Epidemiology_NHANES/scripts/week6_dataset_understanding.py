"""
Project:
    Association Between Cigarette Smoking and Diabetes Among US Adults

Dataset:
    NHANES 2017–March 2020 Pre-Pandemic

Script:
    week6_dataset_understanding.py

Purpose:
    Profile the four NHANES source datasets and document their structure,
    variables, data types, missingness, duplicate rows, and memory usage.

Author:
    Augustine Nkwocha

Version:
    1.0
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import pandas as pd


# =============================================================================
# PROJECT CONFIGURATION
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"

SUMMARY_OUTPUT_PATH = (
    REPORTS_DIR / "week6_dataset_understanding_summary.csv"
)

VARIABLE_OUTPUT_PATH = (
    REPORTS_DIR / "week6_dataset_variable_inventory.csv"
)

MISSINGNESS_OUTPUT_PATH = (
    REPORTS_DIR / "week6_dataset_missingness_summary.csv"
)

REPORT_OUTPUT_PATH = (
    REPORTS_DIR / "week6_dataset_understanding_report.md"
)

LOG_OUTPUT_PATH = (
    LOGS_DIR / "week6_dataset_understanding.log"
)

EXPECTED_IDENTIFIER = "SEQN"

REQUIRED_FILES = {
    "demographics": "P_DEMO.xpt",
    "body_measures": "P_BMX.xpt",
    "smoking": "P_SMQ.xpt",
    "diabetes": "P_DIQ.xpt",
}


# =============================================================================
# DIRECTORY AND LOGGING SETUP
# =============================================================================

def create_output_directories() -> None:
    """
    Create directories used for generated reports and log files.
    """

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


def configure_logging() -> None:
    """
    Configure logging to the terminal and a project log file.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(
                LOG_OUTPUT_PATH,
                mode="w",
                encoding="utf-8",
            ),
        ],
        force=True,
    )


# =============================================================================
# INPUT VALIDATION
# =============================================================================

def validate_inputs() -> dict[str, Path]:
    """
    Confirm that the raw-data directory and required files exist.

    Returns
    -------
    dict[str, Path]
        Mapping of dataset names to verified file paths.
    """

    if not RAW_DATA_DIR.exists():
        raise FileNotFoundError(
            f"Raw-data directory not found: {RAW_DATA_DIR}"
        )

    if not RAW_DATA_DIR.is_dir():
        raise NotADirectoryError(
            f"Expected a directory but found: {RAW_DATA_DIR}"
        )

    verified_files: dict[str, Path] = {}
    missing_files: list[str] = []

    for dataset_name, file_name in REQUIRED_FILES.items():
        file_path = RAW_DATA_DIR / file_name

        if file_path.is_file():
            verified_files[dataset_name] = file_path
        else:
            missing_files.append(file_name)

    if missing_files:
        raise FileNotFoundError(
            "Missing required NHANES files: "
            f"{missing_files}"
        )

    assert len(verified_files) == len(REQUIRED_FILES), (
        "Verified file count does not match required file count."
    )

    logging.info(
        "All %d required input files were verified.",
        len(verified_files),
    )

    return verified_files


# =============================================================================
# DATA LOADING
# =============================================================================

def load_dataset(
    dataset_name: str,
    file_path: Path,
) -> pd.DataFrame:
    """
    Load one NHANES SAS transport dataset.
    """

    logging.info(
        "Loading '%s' from %s",
        dataset_name,
        file_path.name,
    )

    dataframe = pd.read_sas(
        file_path,
        format="xport",
        encoding="utf-8",
    )

    if dataframe.empty:
        raise ValueError(
            f"Dataset '{dataset_name}' contains no observations."
        )

    if EXPECTED_IDENTIFIER not in dataframe.columns:
        raise KeyError(
            f"Identifier '{EXPECTED_IDENTIFIER}' was not found "
            f"in dataset '{dataset_name}'."
        )

    logging.info(
        "Loaded '%s': %d rows and %d columns.",
        dataset_name,
        dataframe.shape[0],
        dataframe.shape[1],
    )

    return dataframe


# =============================================================================
# DATASET PROFILING
# =============================================================================

def create_dataset_summary(
    dataset_name: str,
    file_path: Path,
    dataframe: pd.DataFrame,
) -> dict[str, object]:
    """
    Create one dataset-level profile record.
    """

    total_cells = dataframe.shape[0] * dataframe.shape[1]
    total_missing = int(dataframe.isna().sum().sum())

    missing_percentage = (
        (total_missing / total_cells) * 100
        if total_cells > 0
        else 0.0
    )

    memory_bytes = int(
        dataframe.memory_usage(deep=True).sum()
    )

    return {
        "dataset_name": dataset_name,
        "file_name": file_path.name,
        "rows": dataframe.shape[0],
        "columns": dataframe.shape[1],
        "duplicate_rows": int(dataframe.duplicated().sum()),
        "missing_identifier_values": int(
            dataframe[EXPECTED_IDENTIFIER].isna().sum()
        ),
        "duplicate_identifier_values": int(
            dataframe[EXPECTED_IDENTIFIER].duplicated().sum()
        ),
        "total_missing_values": total_missing,
        "missing_percentage": round(missing_percentage, 2),
        "memory_usage_bytes": memory_bytes,
    }


def create_variable_inventory(
    dataset_name: str,
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create a variable-level inventory for one dataset.
    """

    inventory = pd.DataFrame(
        {
            "dataset_name": dataset_name,
            "variable_name": dataframe.columns,
            "data_type": [
                str(dataframe[column].dtype)
                for column in dataframe.columns
            ],
            "non_missing_values": [
                int(dataframe[column].notna().sum())
                for column in dataframe.columns
            ],
            "missing_values": [
                int(dataframe[column].isna().sum())
                for column in dataframe.columns
            ],
            "unique_values": [
                int(dataframe[column].nunique(dropna=True))
                for column in dataframe.columns
            ],
        }
    )

    inventory["missing_percentage"] = (
        inventory["missing_values"]
        / len(dataframe)
        * 100
    ).round(2)

    return inventory


def create_missingness_summary(
    dataset_name: str,
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create a variable-level missingness summary.
    """

    missingness = pd.DataFrame(
        {
            "dataset_name": dataset_name,
            "variable_name": dataframe.columns,
            "missing_values": dataframe.isna().sum().values,
        }
    )

    missingness["missing_percentage"] = (
        missingness["missing_values"]
        / len(dataframe)
        * 100
    ).round(2)

    return missingness.sort_values(
        by="missing_percentage",
        ascending=False,
    ).reset_index(drop=True)


# =============================================================================
# OUTPUT CREATION
# =============================================================================

def save_csv_outputs(
    dataset_summary: pd.DataFrame,
    variable_inventory: pd.DataFrame,
    missingness_summary: pd.DataFrame,
) -> None:
    """
    Save all structured dataset-understanding outputs.
    """

    dataset_summary.to_csv(
        SUMMARY_OUTPUT_PATH,
        index=False,
    )

    variable_inventory.to_csv(
        VARIABLE_OUTPUT_PATH,
        index=False,
    )

    missingness_summary.to_csv(
        MISSINGNESS_OUTPUT_PATH,
        index=False,
    )

    logging.info(
        "Dataset summary saved to: %s",
        SUMMARY_OUTPUT_PATH,
    )

    logging.info(
        "Variable inventory saved to: %s",
        VARIABLE_OUTPUT_PATH,
    )

    logging.info(
        "Missingness summary saved to: %s",
        MISSINGNESS_OUTPUT_PATH,
    )


def create_markdown_report(
    dataset_summary: pd.DataFrame,
    variable_inventory: pd.DataFrame,
    missingness_summary: pd.DataFrame,
) -> None:
    """
    Generate a human-readable Markdown dataset-understanding report.
    """

    report_lines: list[str] = [
        "# Week 6 Dataset Understanding Report",
        "",
        "## Project",
        "",
        (
            "Association Between Cigarette Smoking and Diabetes "
            "Among US Adults Using NHANES 2017–March 2020 "
            "Pre-Pandemic Data"
        ),
        "",
        "## Dataset-Level Summary",
        "",
        dataset_summary.to_markdown(index=False),
        "",
    ]

    for dataset_name in REQUIRED_FILES:
        dataset_variables = variable_inventory[
            variable_inventory["dataset_name"] == dataset_name
        ]

        dataset_missingness = missingness_summary[
            missingness_summary["dataset_name"] == dataset_name
        ].head(10)

        report_lines.extend(
            [
                f"## {dataset_name.replace('_', ' ').title()}",
                "",
                "### Variables",
                "",
                dataset_variables[
                    [
                        "variable_name",
                        "data_type",
                        "non_missing_values",
                        "missing_values",
                        "missing_percentage",
                        "unique_values",
                    ]
                ].to_markdown(index=False),
                "",
                "### Variables With the Highest Missingness",
                "",
                dataset_missingness[
                    [
                        "variable_name",
                        "missing_values",
                        "missing_percentage",
                    ]
                ].to_markdown(index=False),
                "",
            ]
        )

    REPORT_OUTPUT_PATH.write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )

    logging.info(
        "Markdown report saved to: %s",
        REPORT_OUTPUT_PATH,
    )


# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def main() -> None:
    """
    Run the Week 6 dataset-understanding workflow.
    """

    create_output_directories()
    configure_logging()

    logging.info("=" * 72)
    logging.info("WEEK 6 DATASET UNDERSTANDING STARTED")
    logging.info("=" * 72)

    verified_files = validate_inputs()

    dataset_summary_records: list[dict[str, object]] = []
    variable_inventory_frames: list[pd.DataFrame] = []
    missingness_frames: list[pd.DataFrame] = []

    for dataset_name, file_path in verified_files.items():
        dataframe = load_dataset(
            dataset_name=dataset_name,
            file_path=file_path,
        )

        dataset_summary_records.append(
            create_dataset_summary(
                dataset_name=dataset_name,
                file_path=file_path,
                dataframe=dataframe,
            )
        )

        variable_inventory_frames.append(
            create_variable_inventory(
                dataset_name=dataset_name,
                dataframe=dataframe,
            )
        )

        missingness_frames.append(
            create_missingness_summary(
                dataset_name=dataset_name,
                dataframe=dataframe,
            )
        )

    dataset_summary = pd.DataFrame(
        dataset_summary_records
    )

    variable_inventory = pd.concat(
        variable_inventory_frames,
        ignore_index=True,
    )

    missingness_summary = pd.concat(
        missingness_frames,
        ignore_index=True,
    )

    assert len(dataset_summary) == len(REQUIRED_FILES), (
        "Not all required datasets were summarized."
    )

    assert not variable_inventory.empty, (
        "Variable inventory must not be empty."
    )

    assert not missingness_summary.empty, (
        "Missingness summary must not be empty."
    )

    save_csv_outputs(
        dataset_summary=dataset_summary,
        variable_inventory=variable_inventory,
        missingness_summary=missingness_summary,
    )

    create_markdown_report(
        dataset_summary=dataset_summary,
        variable_inventory=variable_inventory,
        missingness_summary=missingness_summary,
    )

    logging.info("Dataset-level summary:")
    logging.info(
        "\n%s",
        dataset_summary.to_string(index=False),
    )

    logging.info("=" * 72)
    logging.info(
        "WEEK 6 DATASET UNDERSTANDING COMPLETED SUCCESSFULLY"
    )
    logging.info("=" * 72)


# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.exception(
            "Week 6 dataset understanding failed."
        )
        raise