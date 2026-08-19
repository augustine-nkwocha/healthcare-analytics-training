"""
Project:
    Association Between Cigarette Smoking and Diabetes Among US Adults

Dataset:
    NHANES 2017 - March 2020 Pre-Pandemic

Script:
    week6_data_acquisition.py

Purpose:
    Verify that the required NHANES source files are available,
    load them safely, perform basic integrity checks, and export
    a data-acquisition summary.

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
# PROJECT PATHS AND CONFIGURATION
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"

SUMMARY_OUTPUT_PATH = REPORTS_DIR / "week6_data_acquisition_summary.csv"
LOG_OUTPUT_PATH = LOGS_DIR / "week6_data_acquisition.log"

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
    Create output directories used by the acquisition script.
    """

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


def configure_logging() -> None:
    """
    Configure logging to both the terminal and a log file.
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

def validate_raw_data_directory() -> None:
    """
    Confirm that the raw-data directory exists and is a directory.

    Raises
    ------
    FileNotFoundError
        If the raw-data directory does not exist.

    NotADirectoryError
        If the expected path exists but is not a directory.
    """

    if not RAW_DATA_DIR.exists():
        raise FileNotFoundError(
            f"Raw-data directory not found: {RAW_DATA_DIR}"
        )

    if not RAW_DATA_DIR.is_dir():
        raise NotADirectoryError(
            f"Expected a directory but found: {RAW_DATA_DIR}"
        )

    logging.info("Raw-data directory verified: %s", RAW_DATA_DIR)


def validate_required_files() -> dict[str, Path]:
    """
    Confirm that every required NHANES file exists.

    Returns
    -------
    dict[str, Path]
        Mapping of dataset names to verified file paths.

    Raises
    ------
    FileNotFoundError
        If one or more required files are missing.
    """

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
            f"{missing_files}. Expected location: {RAW_DATA_DIR}"
        )

    assert len(verified_files) == len(REQUIRED_FILES), (
        "The number of verified files does not match the number "
        "of required files."
    )

    logging.info(
        "All %d required NHANES files were found.",
        len(verified_files),
    )

    return verified_files


# =============================================================================

# DATA LOADING AND BASIC VALIDATION
# =============================================================================

def load_xpt_file(
    dataset_name: str,
    file_path: Path,
) -> pd.DataFrame:
    """
    Load one NHANES SAS transport file.

    Parameters
    ----------
    dataset_name:
        Logical dataset name used in logs and reports.

    file_path:
        Path to the XPT file.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.

    Raises
    ------
    ValueError
        If the loaded dataset contains no rows or columns.
    """

    logging.info(
        "Loading dataset '%s' from %s",
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
            f"Dataset '{dataset_name}' loaded but contains no records."
        )

    if dataframe.shape[1] == 0:
        raise ValueError(
            f"Dataset '{dataset_name}' contains no variables."
        )

    assert dataframe.shape[0] > 0, (
        f"Dataset '{dataset_name}' must contain at least one row."
    )

    assert dataframe.shape[1] > 0, (
        f"Dataset '{dataset_name}' must contain at least one column."
    )

    logging.info(
        "Loaded '%s': %d rows and %d columns.",
        dataset_name,
        dataframe.shape[0],
        dataframe.shape[1],
    )

    return dataframe


def validate_identifier(
    dataset_name: str,
    dataframe: pd.DataFrame,
) -> None:
    """
    Confirm that the NHANES participant identifier exists.
    """

    if EXPECTED_IDENTIFIER not in dataframe.columns:
        raise KeyError(
            f"Identifier '{EXPECTED_IDENTIFIER}' was not found "
            f"in dataset '{dataset_name}'."
        )

    logging.info(
        "Identifier '%s' verified in '%s'.",
        EXPECTED_IDENTIFIER,
        dataset_name,
    )


# =============================================================================
# SUMMARY CREATION
# =============================================================================

def create_summary_record(
    dataset_name: str,
    file_path: Path,
    dataframe: pd.DataFrame,
) -> dict[str, object]:
    """
    Create one acquisition-summary record.
    """

    identifier = dataframe[EXPECTED_IDENTIFIER]

    return {
        "dataset_name": dataset_name,
        "file_name": file_path.name,
        "file_size_bytes": file_path.stat().st_size,
        "rows": dataframe.shape[0],
        "columns": dataframe.shape[1],
        "identifier": EXPECTED_IDENTIFIER,
        "missing_identifier_values": int(identifier.isna().sum()),
        "duplicate_identifier_values": int(identifier.duplicated().sum()),
    }


def save_acquisition_summary(
    summary_records: list[dict[str, object]],
) -> pd.DataFrame:
    """
    Save the acquisition summary to the reports directory.

    Returns
    -------
    pandas.DataFrame
        Acquisition summary table.
    """

    summary = pd.DataFrame(summary_records)

    expected_columns = {
        "dataset_name",
        "file_name",
        "rows",
        "columns",
        "missing_identifier_values",
        "duplicate_identifier_values",
    }

    missing_columns = expected_columns - set(summary.columns)

    assert not missing_columns, (
        "Acquisition summary is missing expected columns: "
        f"{sorted(missing_columns)}"
    )

    summary.to_csv(
        SUMMARY_OUTPUT_PATH,
        index=False,
    )

    logging.info(
        "Acquisition summary saved to: %s",
        SUMMARY_OUTPUT_PATH,
    )

    return summary


# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def main() -> None:
    """
    Run the Week 6 data-acquisition and verification workflow.
    """

    create_output_directories()
    configure_logging()

    logging.info("=" * 70)
    logging.info("WEEK 6 DATA ACQUISITION STARTED")
    logging.info("=" * 70)

    logging.info("Project root: %s", PROJECT_ROOT)

    validate_raw_data_directory()

    verified_files = validate_required_files()

    loaded_datasets: dict[str, pd.DataFrame] = {}
    summary_records: list[dict[str, object]] = []

    for dataset_name, file_path in verified_files.items():
        dataframe = load_xpt_file(
            dataset_name=dataset_name,
            file_path=file_path,
        )

        validate_identifier(
            dataset_name=dataset_name,
            dataframe=dataframe,
        )

        loaded_datasets[dataset_name] = dataframe

        summary_records.append(
            create_summary_record(
                dataset_name=dataset_name,
                file_path=file_path,
                dataframe=dataframe,
            )
        )

    assert set(loaded_datasets) == set(REQUIRED_FILES), (
        "Not all required datasets were loaded."
    )

    summary = save_acquisition_summary(summary_records)

    logging.info("Acquisition summary:\n%s", summary.to_string(index=False))

    logging.info("=" * 70)
    logging.info("WEEK 6 DATA ACQUISITION COMPLETED SUCCESSFULLY")
    logging.info("=" * 70)


# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.exception("Week 6 data acquisition failed.")
        raise