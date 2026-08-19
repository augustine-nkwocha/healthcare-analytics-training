"""
Project:
    Association Between Cigarette Smoking and Diabetes Among US Adults

Dataset:
    NHANES 2017–March 2020 Pre-Pandemic

Script:
    week6_research_dataset_creation.py

Purpose:
    Select study variables from the required NHANES component files,
    merge participant records using SEQN, restrict the research population
    to adults aged 18 years or older, and save the resulting research dataset.

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
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"

OUTPUT_DATA_PATH = (
    PROCESSED_DATA_DIR / "week6_research_dataset.csv"
)

MERGE_REPORT_PATH = (
    REPORTS_DIR / "week6_research_dataset_creation_summary.csv"
)

LOG_OUTPUT_PATH = (
    LOGS_DIR / "week6_research_dataset_creation.log"
)

ADULT_AGE_THRESHOLD = 18

DATASETS = {
    "demographics": {
        "file": "P_DEMO.xpt",
        "variables": [
            "SEQN",
            "RIDAGEYR",
            "RIAGENDR",
            "WTMECPRP",
            "SDMVPSU",
            "SDMVSTRA",
        ],
    },
    "smoking": {
        "file": "P_SMQ.xpt",
        "variables": [
            "SEQN",
            "SMQ020",
            "SMQ040",
        ],
    },
    "diabetes": {
        "file": "P_DIQ.xpt",
        "variables": [
            "SEQN",
            "DIQ010",
        ],
    },
    "body_measures": {
        "file": "P_BMX.xpt",
        "variables": [
            "SEQN",
            "BMXBMI",
        ],
    },
}


# =============================================================================
# SETUP
# =============================================================================

def create_output_directories() -> None:
    """Create directories required for generated outputs."""

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


def configure_logging() -> None:
    """Configure terminal and file logging."""

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
# DATA LOADING AND SELECTION
# =============================================================================

def load_and_select(
    dataset_name: str,
    file_name: str,
    variables: list[str],
) -> pd.DataFrame:
    """
    Load one NHANES component and retain only required study variables.
    """

    file_path = RAW_DATA_DIR / file_name

    if not file_path.is_file():
        raise FileNotFoundError(
            f"Required file not found: {file_path}"
        )

    dataframe = pd.read_sas(
        file_path,
        format="xport",
        encoding="utf-8",
    )

    missing_variables = (
        set(variables) - set(dataframe.columns)
    )

    if missing_variables:
        raise KeyError(
            f"{dataset_name} is missing required variables: "
            f"{sorted(missing_variables)}"
        )

    selected = dataframe[variables].copy()

    if selected["SEQN"].isna().any():
        raise ValueError(
            f"{dataset_name} contains missing SEQN values."
        )

    if selected["SEQN"].duplicated().any():
        raise ValueError(
            f"{dataset_name} contains duplicate SEQN values."
        )

    logging.info(
        "%s selected: %d rows × %d columns.",

dataset_name,
        selected.shape[0],
        selected.shape[1],
    )

    return selected


# =============================================================================
# MERGING
# =============================================================================

def merge_component(
    base: pd.DataFrame,
    component: pd.DataFrame,
    component_name: str,
) -> tuple[pd.DataFrame, dict[str, object]]:
    """
    Left-merge one NHANES component onto the participant base dataset.
    """

    before_rows = len(base)

    component_variables = [
        column
        for column in component.columns
        if column != "SEQN"
    ]

    merged = base.merge(
        component,
        on="SEQN",
        how="left",
        validate="one_to_one",
        indicator=True,
    )

    matched = int(
        (merged["_merge"] == "both").sum()
    )

    unmatched = int(
        (merged["_merge"] == "left_only").sum()
    )

    merged = merged.drop(columns="_merge")

    assert len(merged) == before_rows, (
        f"Row count changed after merging {component_name}."
    )

    summary = {
        "component": component_name,
        "base_rows_before_merge": before_rows,
        "component_rows": len(component),
        "matched_participants": matched,
        "unmatched_participants": unmatched,
        "variables_added": len(component_variables),
        "rows_after_merge": len(merged),
    }

    logging.info(
        "%s merge: %d matched, %d unmatched.",
        component_name,
        matched,
        unmatched,
    )

    return merged, summary


# =============================================================================
# STUDY POPULATION
# =============================================================================

def restrict_to_adults(
    dataframe: pd.DataFrame,
) -> tuple[pd.DataFrame, dict[str, int]]:
    """
    Restrict the research dataset to participants aged 18 years or older.
    """

    if "RIDAGEYR" not in dataframe.columns:
        raise KeyError(
            "RIDAGEYR is required to define the adult study population."
        )

    if dataframe["RIDAGEYR"].isna().any():
        raise ValueError(
            "RIDAGEYR contains missing values; adult eligibility "
            "cannot be determined for all participants."
        )

    rows_before = len(dataframe)

    adult_data = dataframe.loc[
        dataframe["RIDAGEYR"] >= ADULT_AGE_THRESHOLD
    ].copy()

    rows_after = len(adult_data)

    summary = {
        "participants_before_age_restriction": rows_before,
        "participants_excluded_age_under_18": (
            rows_before - rows_after
        ),
        "adult_participants_retained": rows_after,
    }

    logging.info(
        "Adult restriction: %d retained from %d participants.",
        rows_after,
        rows_before,
    )

    return adult_data, summary


# =============================================================================
# OUTPUT
# =============================================================================

def save_research_dataset(
    dataframe: pd.DataFrame,
) -> None:
    """Save the constructed research dataset."""

    expected_columns = {
        "SEQN",
        "RIDAGEYR",
        "RIAGENDR",
        "WTMECPRP",
        "SDMVPSU",
        "SDMVSTRA",
        "SMQ020",
        "SMQ040",
        "DIQ010",
        "BMXBMI",
    }

    missing_columns = (
        expected_columns - set(dataframe.columns)
    )

    assert not missing_columns, (
        f"Research dataset is missing columns: "
        f"{sorted(missing_columns)}"
    )

    assert dataframe["SEQN"].is_unique, (
        "SEQN must remain unique in the research dataset."
    )

    assert (dataframe["RIDAGEYR"] >= 18).all(), (
        "Research dataset contains participants under age 18."
    )

    dataframe.to_csv(
        OUTPUT_DATA_PATH,
        index=False,
    )

    logging.info(
        "Research dataset saved to: %s",
        OUTPUT_DATA_PATH,
    )


def save_creation_summary(
    merge_summaries: list[dict[str, object]],
    population_summary: dict[str, int],
) -> None:
    """Save merge and population-construction audit information."""

    summary = pd.DataFrame(merge_summaries)

    for key, value in population_summary.items():
        summary[key] = value

    summary.to_csv(
        MERGE_REPORT_PATH,
        index=False,
    )

    logging.info(
        "Research dataset creation summary saved to: %s",
        MERGE_REPORT_PATH,
    )


# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def main() -> None:
    """Run the Week 6 research-dataset construction workflow."""

    create_output_directories()
    configure_logging()

    logging.info("=" * 72)
    logging.info("WEEK 6 RESEARCH DATASET CREATION STARTED")
    logging.info("=" * 72)

    loaded = {}

    for dataset_name, specification in DATASETS.items():
        loaded[dataset_name] = load_and_select(
            dataset_name=dataset_name,
            file_name=specification["file"],
            variables=specification["variables"],
        )

    research_data = loaded["demographics"].copy()

    merge_summaries = []

    for component_name in [
        "smoking",
        "diabetes",
        "body_measures",
    ]:
        research_data, merge_summary = merge_component(
            base=research_data,
            component=loaded[component_name],
            component_name=component_name,
        )

        merge_summaries.append(merge_summary)

    research_data, population_summary = restrict_to_adults(
        research_data
    )

    save_research_dataset(research_data)

    save_creation_summary(
        merge_summaries=merge_summaries,
        population_summary=population_summary,
    )

    logging.info(
        "Final research dataset dimensions: %d rows × %d columns.",
        research_data.shape[0],
        research_data.shape[1],
    )

    logging.info("=" * 72)
    logging.info(
        "WEEK 6 RESEARCH DATASET CREATION COMPLETED SUCCESSFULLY"
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
            "Week 6 research dataset creation failed."
        )
        raise