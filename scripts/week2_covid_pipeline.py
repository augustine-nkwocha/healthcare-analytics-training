import pandas as pd

def cumulative_case_decreases(df):

    df_sorted = (
        df.sort_values(
            ["Country", "Date_reported"]
        )
    )

    decreases = df_sorted[
        df_sorted.groupby("Country")
        ["Cumulative_cases"]
        .diff() < 0
    ]

    return decreases

def cumulative_case_corrections(df):

    df_sorted = (
        df.sort_values(
            ["Country", "Date_reported"]
        )
    )

    df_sorted["case_change"] = (
        df_sorted
        .groupby("Country")
        ["Cumulative_cases"]
        .diff()
    )

    return df_sorted[
        df_sorted["case_change"] < 0
    ]

df = pd.read_csv(
    "data/raw/WHO-COVID-19-global-daily-data.csv"
)


df["Date_reported"] = pd.to_datetime(
    df["Date_reported"]
)

print("\n")
print("=" * 50)
print("DATE TYPE AFTER CONVERSION")
print("=" * 50)

print(
    df["Date_reported"].dtype
)

df["year"] = df["Date_reported"].dt.year

def yearly_missing_percent(df, column):

    result = (
        df.groupby("year")[column]
        .apply(
            lambda x:
            round(
                x.isna().mean() * 100,
                2
            )
        )
    )

    return result



print("\n")
print("=" * 50)
print("MISSING CASES BY YEAR")
print("=" * 50)

print(
    df.groupby("year")["New_cases"]
    .apply(lambda x: x.isna().sum())
)

print("\n")
print("=" * 50)
print("MISSING NEW DEATHS BY YEAR")
print("=" * 50)

print(
    df.groupby("year")["New_deaths"]
    .apply(lambda x: x.isna().sum())
)

print("\n")
print("=" * 50)
print("NEW CASES MISSING (%) BY YEAR")
print("=" * 50)

print(
    yearly_missing_percent(
        df,
        "New_cases"
    )
)

print("\n")
print("=" * 50)
print("NEW DEATHS MISSING (%) BY YEAR")
print("=" * 50)

print(
    yearly_missing_percent(
        df,
        "New_deaths"
    )
)

print("\n")
print("=" * 50)
print("CUMULATIVE CASE DECREASES")
print("=" * 50)

case_decreases = (
    cumulative_case_decreases(df)
)

print(
    "Records:",
    len(case_decreases)
)

print("\n")
print("=" * 50)
print("CUMULATIVE CASE DECREASE SAMPLE")
print("=" * 50)

print(
    case_decreases[
        [
            "Country",
            "Date_reported",
            "Cumulative_cases"
        ]
    ].head(10)
)

corrections = cumulative_case_corrections(df)

print("\n")
print("=" * 50)
print("LARGEST CUMULATIVE CASE CORRECTIONS")
print("=" * 50)

print(
    corrections[
        [
            "Country",
            "Date_reported",
            "case_change"
        ]
    ]
    .sort_values(
        "case_change"
    )
    .head(10)
)

nigeria = df[
    df["Country"] == "Nigeria"
]

print("\n")
print("=" * 50)
print("NIGERIA DATASET")
print("=" * 50)

print(
    nigeria.shape
)

print("\n")
print("=" * 50)
print("NIGERIA DATE RANGE")
print("=" * 50)

print(
    nigeria["Date_reported"].min()
)

print(
    nigeria["Date_reported"].max()
)

print("\n")
print("=" * 50)
print("NIGERIA MISSINGNESS")
print("=" * 50)

print(
    nigeria[
        [
            "New_cases",
            "New_deaths"
        ]
    ]
    .isna()
    .sum()
)

print("\n")
print("=" * 50)
print("NIGERIA MISSINGNESS (%)")
print("=" * 50)

print(
    round(
        nigeria[
            [
                "New_cases",
                "New_deaths"
            ]
        ]
        .isna()
        .mean() * 100,
        2
    )
)

print("\n")
print("=" * 50)
print("NIGERIA NEW CASES MISSING (%) BY YEAR")
print("=" * 50)

print(
    yearly_missing_percent(
        nigeria,
        "New_cases"
    )
)

print("\n")
print("=" * 50)
print("NIGERIA NEW DEATHS MISSING (%) BY YEAR")
print("=" * 50)

print(
    yearly_missing_percent(
        nigeria,
        "New_deaths"
    )
)

nigeria_2020_2021 = nigeria[
    nigeria["year"].isin([2020, 2021])
].copy()

print("\n")
print("=" * 50)
print("NIGERIA 2020-2021 DATASET")
print("=" * 50)

print(nigeria_2020_2021.shape)


print("\n")
print("=" * 50)
print("NEW CASES MISSING (%)")
print("=" * 50)

print(
    round(
        nigeria_2020_2021["New_cases"]
        .isna()
        .mean() * 100,
        2
    )
)

# =====================
# BASIC PROFILE
# =====================

print("\n")
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
print("DATA TYPES")
print("=" * 50)

print(df.dtypes)

print("\n")
print("=" * 50)
print("MISSING VALUES")
print("=" * 50)

missing = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percent":
        round(
            (df.isna().sum() / len(df)) * 100,
            2
        )
})

print(
    missing.sort_values(
        "missing_percent",
        ascending=False
    )
)

print("\n")
print("=" * 50)
print("DATE RANGE")
print("=" * 50)

print(
    df["Date_reported"].min()
)

print(
    df["Date_reported"].max()
)