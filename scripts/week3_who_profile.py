import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = (
    "data/raw/who_gho_life_expectancy.csv"
)

def load_data():
    df = pd.read_csv(INPUT_PATH)

    assert df.shape[0] > 0
    assert "Indicator" in df.columns

    logging.info(
        f"Loaded dataset with shape {df.shape}"
    )

    return df

def inspect_dataset(df):

    print("\n")
    print("=" * 50)
    print("DATASET SHAPE")
    print("=" * 50)
    print(df.shape)

    print("\n")
    print("=" * 50)
    print("INFO")
    print("=" * 50)
    print(df.info())

    print("\n")
    print("=" * 50)
    print("MISSINGNESS")
    print("=" * 50)
    print(df.isna().sum())

    print("\n")
    print("=" * 50)
    print("DUPLICATES")
    print("=" * 50)
    print(df.duplicated().sum())

    print("\n")
    print("=" * 50)
    print("NUMBER OF INDICATORS")
    print("=" * 50)
    print(
        df["Indicator"]
        .nunique()
    )

    print("\n")
    print("=" * 50)
    print("NUMBER OF INDICATORS")
    print("=" * 50)
    print(
        df["Indicator"]
        .value_counts(dropna = False)
    )

    print("\n")
    print("=" * 50)
    print("SEX CATEGORIES")
    print("=" * 50)
    print(
        df["Dim1"]
        .value_counts(dropna = False)
    )

    print("\n")
    print("=" * 50)
    print("NUMBER OF COUNTRIES")
    print("=" * 50)
    print(
        df["Location"]
        .nunique()
    )

    print("\n")
    print("=" * 50)
    print("REGIONS")
    print("=" * 50)
    print(
        df["ParentLocation"]
        .value_counts(dropna = False)
    )

    print("\n")
    print("=" * 50)
    print("YEAR RANGE")
    print("=" * 50)
    print(
        df["Period"].min(),
        df["Period"].max()
    )

    logging.info(
        "Dataset inspection completed"
    )

def main():

    df = load_data()
    inspect_dataset(df)

if __name__ == "__main__":
    main()









