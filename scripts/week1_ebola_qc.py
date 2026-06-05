import pandas as pd

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

# =====================
# LOAD DATA
# =====================

df = pd.read_csv("data/raw/linelist_raw.csv")

df = standardize_columns(df)

print("\n")
print("=" * 50)
print("STANDARDIZED COLUMNS")
print("=" * 50)
print(df.columns.tolist())

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
