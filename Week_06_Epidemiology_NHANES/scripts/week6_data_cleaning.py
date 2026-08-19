"""
Project:
    Association Between Cigarette Smoking and Diabetes Among US Adults

Dataset:
    NHANES 2017–March 2020 Pre-Pandemic

Script:
    week6_data_cleaning.py

Purpose:
    Clean the Week 6 research dataset, validate source-variable coding,
    derive analysis variables for sex, smoking status, and diabetes status,
    preserve legitimate and structural missingness, and document all
    cleaning outcomes.

Author:
    Augustine Nkwocha

Version:
    1.0
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd


# =============================================================================
# PROJECT CONFIGURATION
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"

INPUT_DATA_PATH = (
    PROCESSED_DATA_DIR / "week6_research_dataset.csv"
)

OUTPUT_DATA_PATH = (
    PROCESSED_DATA_DIR / "week6_cleaned_dataset.csv"
)

CLEANING_SUMMARY_PATH = (
    REPORTS_DIR / "week6_cleaning_summary.csv"
)

LOG_OUTPUT_PATH = (
    LOGS_DIR / "week6_data_cleaning.log"
)

EXPECTED_COLUMNS = [
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
]


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
# DATA LOADING
# =============================================================================

def load_research_dataset() -> pd.DataFrame:
    """Load and verify the Week 6 research dataset."""

    if not INPUT_DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Research dataset not found: {INPUT_DATA_PATH}"
        )

    dataframe = pd.read_csv(INPUT_DATA_PATH)

    if dataframe.empty:
        raise ValueError(
            "Research dataset contains no observations."
        )

    missing_columns = (
        set(EXPECTED_COLUMNS) - set(dataframe.columns)
    )

    if missing_columns:
        raise KeyError(
            "Research dataset is missing required columns: "
            f"{sorted(missing_columns)}"
        )

    logging.info(
        "Research dataset loaded: %d rows × %d columns.",
        dataframe.shape[0],
        dataframe.shape[1],
    )

    return dataframe


# =============================================================================
# SOURCE DATA VALIDATION
# =============================================================================

def validate_identifier(dataframe: pd.DataFrame) -> None:
    """Validate participant identifier integrity."""

    if dataframe["SEQN"].isna().any():
        raise ValueError("SEQN contains missing values.")

    if dataframe["SEQN"].duplicated().any():
        raise ValueError("SEQN contains duplicate values.")

    logging.info("SEQN validation passed.")


def validate_age(dataframe: pd.DataFrame) -> None:
    """Validate the adult age range."""

    if dataframe["RIDAGEYR"].isna().any():
        raise ValueError("RIDAGEYR contains missing values.")

    invalid_age = ~dataframe["RIDAGEYR"].between(
18,
        80,
        inclusive="both",
    )

    if invalid_age.any():
        raise ValueError(
            f"Found {int(invalid_age.sum())} age values "
            "outside the expected adult range 18–80."
        )

    logging.info("RIDAGEYR validation passed.")


def validate_allowed_codes(
    dataframe: pd.DataFrame,
    column: str,
    allowed_codes: set[float],
    allow_missing: bool = False,
) -> None:
    """
    Validate coded questionnaire or categorical variables.
    """

    observed = set(
        dataframe[column]
        .dropna()
        .unique()
    )

    unexpected = observed - allowed_codes

    if unexpected:
        raise ValueError(
            f"{column} contains unexpected codes: "
            f"{sorted(unexpected)}"
        )

    if not allow_missing and dataframe[column].isna().any():
        raise ValueError(
            f"{column} contains unexpected missing values."
        )

    logging.info(
        "%s coding validation passed.",
        column,
    )


def validate_survey_variables(
    dataframe: pd.DataFrame,
) -> None:
    """Validate required NHANES survey-design variables."""

    for column in [
        "WTMECPRP",
        "SDMVPSU",
        "SDMVSTRA",
    ]:
        if dataframe[column].isna().any():
            raise ValueError(
                f"{column} contains missing values."
            )

    if (dataframe["WTMECPRP"] <= 0).any():
        raise ValueError(
            "WTMECPRP contains non-positive survey weights."
        )

    logging.info(
        "Survey-design variable validation passed."
    )


# =============================================================================
# DERIVED VARIABLES
# =============================================================================

def derive_sex(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Derive a labelled sex variable from RIAGENDR.
    """

    result = dataframe.copy()

    result["sex"] = result["RIAGENDR"].map(
        {
            1.0: "Male",
            2.0: "Female",
        }
    )

    if result["sex"].isna().any():
        raise ValueError(
            "Unable to derive sex for all participants."
        )

    logging.info(
        "Derived variable created: sex."
    )

    return result


def derive_smoking_status(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Derive smoking status from SMQ020 and SMQ040.

    Rules
    -----
    SMQ020 = 2
        Never smoker

    SMQ020 = 1 and SMQ040 = 3
        Former smoker

    SMQ020 = 1 and SMQ040 in {1, 2}
        Current smoker

    SMQ020 in {7, 9} or unresolved combinations
        Missing derived smoking status
    """

    result = dataframe.copy()

    conditions = [
        result["SMQ020"].eq(2.0),

        (
            result["SMQ020"].eq(1.0)
            & result["SMQ040"].eq(3.0)
        ),

        (
            result["SMQ020"].eq(1.0)
            & result["SMQ040"].isin([1.0, 2.0])
        ),
    ]

    choices = [
        "Never",
        "Former",
        "Current",
    ]

    result["smoking_status"] = np.select(
        conditions,
        choices,
        default=None,
    )

    logging.info(
        "Derived variable created: smoking_status."
    )

    return result


def derive_diabetes_status(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Derive the primary binary diabetes outcome from DIQ010.

    Rules
    -----
    DIQ010 = 1
        Diabetes

    DIQ010 = 2
        No diabetes

    DIQ010 = 3
        Borderline; unresolved for primary binary outcome

    DIQ010 in {7, 9}
        Missing / unknown
    """

    result = dataframe.copy()

    result["diabetes_status"] = result["DIQ010"].map(
        {
            1.0: "Diabetes",
            2.0: "No diabetes",
        }
    )

    logging.info(
        "Derived variable created: diabetes_status."
    )

    return result


# =============================================================================
# POST-CLEANING VALIDATION
# =============================================================================

def validate_derived_variables(
    dataframe: pd.DataFrame,
) -> None:
    """Validate derived analytical variables."""

    smoking_categories = set(
        dataframe["smoking_status"]
        .dropna()
        .unique()
    )

    expected_smoking_categories = {
        "Never",
        "Former",
        "Current",
    }

    if not smoking_categories.issubset(
        expected_smoking_categories
    ):
        raise ValueError(
            "Unexpected smoking-status categories found."
        )

    diabetes_categories = set(
        dataframe["diabetes_status"]
        .dropna()
        .unique()
    )

    expected_diabetes_categories = {
        "Diabetes",
        "No diabetes",
    }

    if not diabetes_categories.issubset(
        expected_diabetes_categories
    ):
        raise ValueError(
            "Unexpected diabetes-status categories found."
        )

    assert dataframe["SEQN"].is_unique, (
        "SEQN uniqueness was lost during cleaning."
    )

    logging.info(
        "Derived-variable validation passed."
    )


# =============================================================================
# CLEANING SUMMARY
# =============================================================================

def create_cleaning_summary(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Create a structured summary of cleaning outcomes."""

    smoking_counts = (
        dataframe["smoking_status"]
        .value_counts(dropna=False)
    )

    diabetes_counts = (
        dataframe["diabetes_status"]
        .value_counts(dropna=False)
    )

    summary_records = [
        {
            "check": "total_adult_participants",
            "count": len(dataframe),
        },
        {
            "check": "male",
            "count": int(
                (dataframe["sex"] == "Male").sum()
            ),
        },
        {
            "check": "female",
            "count": int(
                (dataframe["sex"] == "Female").sum()
            ),
        },
        {
            "check": "never_smokers",
            "count": int(
                smoking_counts.get("Never", 0)
            ),
        },
        {
            "check": "former_smokers",
            "count": int(
                smoking_counts.get("Former", 0)
            ),
        },
        {
            "check": "current_smokers",
            "count": int(
                smoking_counts.get("Current", 0)
            ),
        },
        {
            "check": "unresolved_smoking_status",
            "count": int(
                dataframe["smoking_status"]
                .isna()
                .sum()
            ),
        },
        {
            "check": "diabetes",
            "count": int(
                diabetes_counts.get("Diabetes", 0)
            ),
        },
        {
            "check": "no_diabetes",
            "count": int(
                diabetes_counts.get("No diabetes", 0)
            ),
        },
        {
            "check": "unresolved_binary_diabetes_status",
            "count": int(
                dataframe["diabetes_status"]
                .isna()
                .sum()
            ),
        },
        {
            "check": "missing_bmi",
            "count": int(
                dataframe["BMXBMI"]
                .isna()
                .sum()
            ),
        },
        {
            "check": "missing_survey_weight",
            "count": int(
                dataframe["WTMECPRP"]
                .isna()
                .sum()
            ),
        },
    ]

    return pd.DataFrame(summary_records)


# =============================================================================
# OUTPUT
# =============================================================================

def save_outputs(
    dataframe: pd.DataFrame,
    cleaning_summary: pd.DataFrame,
) -> None:
    """Save cleaned data and cleaning audit summary."""

    dataframe.to_csv(
        OUTPUT_DATA_PATH,
        index=False,
    )

    cleaning_summary.to_csv(
        CLEANING_SUMMARY_PATH,
        index=False,
    )

    logging.info(
"Cleaned dataset saved to: %s",
        OUTPUT_DATA_PATH,
    )

    logging.info(
        "Cleaning summary saved to: %s",
        CLEANING_SUMMARY_PATH,
    )


# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def main() -> None:
    """Run the Week 6 data-cleaning workflow."""

    create_output_directories()
    configure_logging()

    logging.info("=" * 72)
    logging.info("WEEK 6 DATA CLEANING STARTED")
    logging.info("=" * 72)

    dataframe = load_research_dataset()

    rows_before_cleaning = len(dataframe)

    # Validate original source variables.
    validate_identifier(dataframe)
    validate_age(dataframe)

    validate_allowed_codes(
        dataframe,
        column="RIAGENDR",
        allowed_codes={1.0, 2.0},
        allow_missing=False,
    )

    validate_allowed_codes(
        dataframe,
        column="SMQ020",
        allowed_codes={1.0, 2.0, 7.0, 9.0},
        allow_missing=False,
    )

    validate_allowed_codes(
        dataframe,
        column="SMQ040",
        allowed_codes={1.0, 2.0, 3.0, 7.0, 9.0},
        allow_missing=True,
    )

    validate_allowed_codes(
        dataframe,
        column="DIQ010",
        allowed_codes={1.0, 2.0, 3.0, 7.0, 9.0},
        allow_missing=True,
    )

    validate_survey_variables(dataframe)

    # Derive analytical variables.
    dataframe = derive_sex(dataframe)
    dataframe = derive_smoking_status(dataframe)
    dataframe = derive_diabetes_status(dataframe)

    # Confirm that cleaning did not accidentally remove participants.
    assert len(dataframe) == rows_before_cleaning, (
        "Participant count changed unexpectedly during cleaning."
    )

    validate_derived_variables(dataframe)

    cleaning_summary = create_cleaning_summary(
        dataframe
    )

    save_outputs(
        dataframe=dataframe,
        cleaning_summary=cleaning_summary,
    )

    logging.info(
        "Rows before cleaning: %d",
        rows_before_cleaning,
    )

    logging.info(
        "Rows after cleaning: %d",
        len(dataframe),
    )

    logging.info(
        "Smoking status:\n%s",
        dataframe["smoking_status"]
        .value_counts(dropna=False)
        .to_string(),
    )

    logging.info(
        "Diabetes status:\n%s",
        dataframe["diabetes_status"]
        .value_counts(dropna=False)
        .to_string(),
    )

    logging.info(
        "Missing BMI: %d",
        dataframe["BMXBMI"].isna().sum(),
    )

    logging.info("=" * 72)
    logging.info(
        "WEEK 6 DATA CLEANING COMPLETED SUCCESSFULLY"
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
            "Week 6 data cleaning failed."
        )
        raise