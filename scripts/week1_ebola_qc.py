import pandas as pd
import re

def missingness_report(df):

    missing = (
        df.isna()
        .sum()
        .sort_values(ascending=False)
    )

    percent = (
        missing / len(df)
    ) * 100

    report = pd.DataFrame({
        "missing_count": missing,
        "missing_percent": percent.round(2)
    })

    return report

def standardize_columns(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df

def convert_dates(df):

    date_cols = [
        "infection_date",
        "date_onset",
        "hosp_date",
        "date_of_outcome"
    ]

    for col in date_cols:

        df[col] = pd.to_datetime(
            df[col],
            errors="coerce"
        )

    return df

def clean_dataset(df):

    df = standardize_columns(df)
    df = convert_dates(df)

    return df

def temporal_qc(df):

    onset_before_infection = (
        df["date_onset"] < df["infection_date"]
    ).sum()

    hosp_before_onset = (
        df["hosp_date"] < df["date_onset"]
    ).sum()

    outcome_before_hosp = (
        df["date_of_outcome"] < df["hosp_date"]
    ).sum()

    return {
        "onset_before_infection":
            onset_before_infection,

        "hosp_before_onset":
            hosp_before_onset,

        "outcome_before_hosp":
            outcome_before_hosp
    }

def outcome_before_hosp_records(df):

    return df[
        df["date_of_outcome"]
        < df["hosp_date"]
    ]

def invalid_time_report(df):

    pattern = r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$"

    invalid = df[
        df["time_admission"]
        .notna()
        &
        ~df["time_admission"]
        .astype(str)
        .str.match(pattern)
    ]

    return invalid     

def duplicate_records(df):

    return df[
        df.duplicated(
            keep=False
        )
    ]

def remove_exact_duplicates(df):

    return df.drop_duplicates()

# =====================
# LOAD DATA
# =====================

df = pd.read_csv("data/raw/linelist_raw.csv")

df = standardize_columns(df)

df = convert_dates(df)

# =====================
# VERIFICATION
# =====================

print("\n")
print("=" * 50)
print("STANDARDIZED COLUMNS")
print("=" * 50)
print(df.columns.tolist())

print("\n")
print("=" * 50)
print("DATE COLUMN TYPES")
print("=" * 50)

print(
    df[
        [
            "infection_date",
            "date_onset",
            "hosp_date",
            "date_of_outcome"
        ]
    ].dtypes
)

print("\n")
print("=" * 50)
print("DATE MISSINGNESS AFTER CONVERSION")
print("=" * 50)

date_cols = [
    "infection_date",
    "date_onset",
    "hosp_date",
    "date_of_outcome"
]

print(df[date_cols].isna().sum())

print("\n")
print("=" * 50)
print("TEMPORAL QC")
print("=" * 50)

print(
    temporal_qc(df)
)

print("\n")
print("=" * 50)
print("OUTCOME BEFORE HOSP SAMPLE")
print("=" * 50)

print(
    outcome_before_hosp_records(df)[
        [
            "case_id",
            "hosp_date",
            "date_of_outcome",
            "outcome"
        ]
    ].head(10)
)

print("\n")
print("=" * 50)
print("OUTCOME BEFORE HOSP PERCENT")
print("=" * 50)

percent = (
    outcome_before_hosp_records(df).shape[0]
    / len(df)
) * 100

print(round(percent, 2))

print("\n")
print("=" * 50)
print("INVALID TIME QC")
print("=" * 50)

invalid_times = invalid_time_report(df)

print(
    "Invalid Times:",
    invalid_times.shape[0]
)

print(
    "Percent:",
    round(
        (
            invalid_times.shape[0]
            / len(df)
        ) * 100,
        2
    )
)

print("\n")
print("=" * 50)
print("INVALID TIME SAMPLE")
print("=" * 50)

print(
    invalid_times[
        ["case_id", "time_admission"]
    ].head(10)
)

print("\n")
print("=" * 50)
print("DUPLICATE RECORDS")
print("=" * 50)

print(
    duplicate_records(df)
)

df = remove_exact_duplicates(df)

# Save cleaned/intermediate dataset
cleaned_path = "data/interim/linelist_cleaned.csv"
df.to_csv(cleaned_path, index=False)

print("\n")
print("=" * 50)
print("CLEANED DATASET SAVED")
print("=" * 50)
print(cleaned_path)

# =====================
# BASIC PROFILE
# =====================

print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n")

print("=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(df.columns.tolist())

print("\n")

print("=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(
    missingness_report(df)
)

print("\n")

print("=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)
print(df.duplicated().sum())


