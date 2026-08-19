"""
Project:
    Association Between Cigarette Smoking and Diabetes Among US Adults

Dataset:
    NHANES 2017–March 2020 Pre-Pandemic

Script:
    week6_validation.py

Purpose:
    Independently validate the cleaned Week 6 research dataset by checking
    participant integrity, study-population rules, derived-variable logic,
    BMI plausibility, survey-design variables, and category reconciliation.

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

PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"

INPUT_DATA_PATH = (
    PROCESSED_DATA_DIR / "week6_cleaned_dataset.csv"
)

VALIDATION_SUMMARY_PATH = (
    REPORTS_DIR / "week6_validation_summary.csv"
)

LOG_OUTPUT_PATH = (
    LOGS_DIR / "week6_validation.log"
)

EXPECTED_COLUMNS = {
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
    "sex",
    "smoking_status",
    "diabetes_status",
}

EXPECTED_ROW_COUNT = 9693


# =============================================================================
# SETUP
# =============================================================================

def create_output_directories() -> None:
    """Create directories required for validation outputs."""

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

def load_cleaned_dataset() -> pd.DataFrame:
    """Load and verify the cleaned Week 6 dataset."""

    if not INPUT_DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {INPUT_DATA_PATH}"
        )

    dataframe = pd.read_csv(INPUT_DATA_PATH)

    if dataframe.empty:
        raise ValueError(
            "Cleaned dataset contains no observations."
        )

    missing_columns = (
        EXPECTED_COLUMNS - set(dataframe.columns)
    )

    if missing_columns:
        raise KeyError(
            "Cleaned dataset is missing required columns: "
            f"{sorted(missing_columns)}"
        )

    logging.info(
        "Cleaned dataset loaded: %d rows × %d columns.",
        dataframe.shape[0],
        dataframe.shape[1],
    )

    return dataframe


# =============================================================================
# VALIDATION HELPERS
# =============================================================================

def add_result(
    results: list[dict[str, object]],
    check_name: str,
    passed: bool,
    observed: object,
    expected: object,
) -> None:
    """Append one validation result."""

    results.append(
        {
            "check": check_name,
            "status": "PASS" if passed else "FAIL",
            "observed": observed,
            "expected": expected,
        }
    )


# =============================================================================
# PARTICIPANT-LEVEL VALIDATION
# =============================================================================

def validate_participant_integrity(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Validate row count and participant identifier integrity."""

    row_count_pass = len(dataframe) == EXPECTED_ROW_COUNT

    add_result(
        results,
        check_name="expected_row_count",
        passed=row_count_pass,
        observed=len(dataframe),
        expected=EXPECTED_ROW_COUNT,
    )

    missing_seqn = int(
        dataframe["SEQN"].isna().sum()
    )

    add_result(
        results,
        check_name="missing_seqn",
        passed=missing_seqn == 0,
        observed=missing_seqn,
        expected=0,
    )

    duplicate_seqn = int(
        dataframe["SEQN"].duplicated().sum()
    )

    add_result(
        results,
        check_name="duplicate_seqn",
        passed=duplicate_seqn == 0,
        observed=duplicate_seqn,
        expected=0,
    )


# =============================================================================
# STUDY POPULATION VALIDATION
# =============================================================================

def validate_study_population(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Validate adult study-population rules."""

    min_age = dataframe["RIDAGEYR"].min()
    max_age = dataframe["RIDAGEYR"].max()

    add_result(
        results,
        check_name="minimum_age",
        passed=min_age >= 18,
        observed=min_age,
        expected=">=18",
    )

    add_result(
        results,
        check_name="maximum_age",
        passed=max_age <= 80,
        observed=max_age,
        expected="<=80",
    )


# =============================================================================
# SEX VALIDATION
# =============================================================================

def validate_sex_derivation(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Confirm that sex labels agree with RIAGENDR coding."""

    expected_sex = dataframe["RIAGENDR"].map(
        {
            1.0: "Male",
            2.0: "Female",
        }
    )

    mismatches = int(
        (expected_sex != dataframe["sex"]).sum()
    )

    add_result(
        results,
        check_name="sex_derivation_mismatches",
        passed=mismatches == 0,
        observed=mismatches,
        expected=0,
    )


# =============================================================================
# SMOKING-STATUS VALIDATION
# =============================================================================

def validate_smoking_derivation(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Validate smoking_status against SMQ020 and SMQ040."""

    never_mask = (
        dataframe["SMQ020"].eq(2.0)
    )

    former_mask = (
        dataframe["SMQ020"].eq(1.0)
        & dataframe["SMQ040"].eq(3.0)
    )

    current_mask = (
        dataframe["SMQ020"].eq(1.0)
        & dataframe["SMQ040"].isin([1.0, 2.0])
    )

    unresolved_mask = ~(
        never_mask
        | former_mask
        | current_mask
    )

    never_mismatch = int(
        (
            never_mask
            & dataframe["smoking_status"].ne("Never")
        ).sum()
    )

    former_mismatch = int(
        (
            former_mask
            & dataframe["smoking_status"].ne("Former")
        ).sum()
    )

    current_mismatch = int(
        (
            current_mask
            & dataframe["smoking_status"].ne("Current")
        ).sum()
    )

    unresolved_mismatch = int(
        (
            unresolved_mask
            & dataframe["smoking_status"].notna()
        ).sum()
    )

    add_result(
        results,
        check_name="never_smoker_derivation_mismatches",
        passed=never_mismatch == 0,
        observed=never_mismatch,
        expected=0,
    )

    add_result(
        results,
        check_name="former_smoker_derivation_mismatches",
        passed=former_mismatch == 0,
        observed=former_mismatch,
        expected=0,
    )

    add_result(
        results,
        check_name="current_smoker_derivation_mismatches",
        passed=current_mismatch == 0,
        observed=current_mismatch,
expected=0,
    )

    add_result(
        results,
        check_name="unresolved_smoking_mismatches",
        passed=unresolved_mismatch == 0,
        observed=unresolved_mismatch,
        expected=0,
    )


# =============================================================================
# DIABETES-STATUS VALIDATION
# =============================================================================

def validate_diabetes_derivation(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Validate diabetes_status against DIQ010."""

    expected_status = dataframe["DIQ010"].map(
        {
            1.0: "Diabetes",
            2.0: "No diabetes",
        }
    )

    both_nonmissing = (
        expected_status.notna()
        & dataframe["diabetes_status"].notna()
    )

    mismatches = int(
        (
            expected_status[both_nonmissing]
            != dataframe.loc[
                both_nonmissing,
                "diabetes_status",
            ]
        ).sum()
    )

    unresolved_expected = expected_status.isna()

    unresolved_mismatch = int(
        (
            unresolved_expected
            & dataframe["diabetes_status"].notna()
        ).sum()
    )

    add_result(
        results,
        check_name="diabetes_derivation_mismatches",
        passed=mismatches == 0,
        observed=mismatches,
        expected=0,
    )

    add_result(
        results,
        check_name="unresolved_diabetes_mismatches",
        passed=unresolved_mismatch == 0,
        observed=unresolved_mismatch,
        expected=0,
    )


# =============================================================================
# BMI VALIDATION
# =============================================================================

def validate_bmi(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Validate observed BMI values and documented missingness."""

    observed_bmi = dataframe["BMXBMI"].dropna()

    missing_bmi = int(
        dataframe["BMXBMI"].isna().sum()
    )

    add_result(
        results,
        check_name="missing_bmi_count",
        passed=missing_bmi == 903,
        observed=missing_bmi,
        expected=903,
    )

    min_bmi = observed_bmi.min()
    max_bmi = observed_bmi.max()

    add_result(
        results,
        check_name="minimum_observed_bmi",
        passed=min_bmi >= 0,
        observed=min_bmi,
        expected=">=0",
    )

    add_result(
        results,
        check_name="maximum_observed_bmi",
        passed=max_bmi <= 100,
        observed=max_bmi,
        expected="<=100",
    )


# =============================================================================
# SURVEY-DESIGN VALIDATION
# =============================================================================

def validate_survey_design(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Validate survey weights, PSU, and strata."""

    missing_weights = int(
        dataframe["WTMECPRP"].isna().sum()
    )

    nonpositive_weights = int(
        (dataframe["WTMECPRP"] <= 0).sum()
    )

    missing_psu = int(
        dataframe["SDMVPSU"].isna().sum()
    )

    missing_strata = int(
        dataframe["SDMVSTRA"].isna().sum()
    )

    add_result(
        results,
        check_name="missing_survey_weights",
        passed=missing_weights == 0,
        observed=missing_weights,
        expected=0,
    )

    add_result(
        results,
        check_name="nonpositive_survey_weights",
        passed=nonpositive_weights == 0,
        observed=nonpositive_weights,
        expected=0,
    )

    add_result(
        results,
        check_name="missing_psu",
        passed=missing_psu == 0,
        observed=missing_psu,
        expected=0,
    )

    add_result(
        results,
        check_name="missing_strata",
        passed=missing_strata == 0,
        observed=missing_strata,
        expected=0,
    )


# =============================================================================
# CATEGORY RECONCILIATION
# =============================================================================

def validate_category_reconciliation(
    dataframe: pd.DataFrame,
    results: list[dict[str, object]],
) -> None:
    """Confirm that derived categories reconcile to the total population."""

    smoking_total = (
        dataframe["smoking_status"]
        .value_counts(dropna=False)
        .sum()
    )

    diabetes_total = (
        dataframe["diabetes_status"]
        .value_counts(dropna=False)
        .sum()
    )

    add_result(
        results,
        check_name="smoking_category_total",
        passed=smoking_total == len(dataframe),
        observed=smoking_total,
        expected=len(dataframe),
    )

    add_result(
        results,
        check_name="diabetes_category_total",
        passed=diabetes_total == len(dataframe),
        observed=diabetes_total,
        expected=len(dataframe),
    )


# =============================================================================
# OUTPUT
# =============================================================================

def save_validation_summary(
    results: list[dict[str, object]],
) -> pd.DataFrame:
    """Save the structured validation summary."""

    summary = pd.DataFrame(results)

    summary.to_csv(
        VALIDATION_SUMMARY_PATH,
        index=False,
    )

    logging.info(
        "Validation summary saved to: %s",
        VALIDATION_SUMMARY_PATH,
    )

    return summary


# =============================================================================
# MAIN WORKFLOW
# =============================================================================

def main() -> None:
    """Run the Week 6 cleaned-data validation workflow."""

    create_output_directories()
    configure_logging()

    logging.info("=" * 72)
    logging.info("WEEK 6 VALIDATION STARTED")
    logging.info("=" * 72)

    dataframe = load_cleaned_dataset()

    results: list[dict[str, object]] = []

    validate_participant_integrity(
        dataframe,
        results,
    )

    validate_study_population(
        dataframe,
        results,
    )

    validate_sex_derivation(
        dataframe,
        results,
    )

    validate_smoking_derivation(
        dataframe,
        results,
    )

    validate_diabetes_derivation(
        dataframe,
        results,
    )

    validate_bmi(
        dataframe,
        results,
    )

    validate_survey_design(
        dataframe,
        results,
    )

    validate_category_reconciliation(
        dataframe,
        results,
    )

    summary = save_validation_summary(results)

    failed_checks = summary[
        summary["status"] == "FAIL"
    ]

    logging.info(
        "Validation results:\n%s",
        summary.to_string(index=False),
    )

    if not failed_checks.empty:
        raise ValueError(
            f"{len(failed_checks)} validation checks failed."
        )

    logging.info(
        "All %d validation checks passed.",
        len(summary),
    )

    logging.info("=" * 72)
    logging.info(
        "WEEK 6 VALIDATION COMPLETED SUCCESSFULLY"
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
            "Week 6 validation failed."
        )
        raise