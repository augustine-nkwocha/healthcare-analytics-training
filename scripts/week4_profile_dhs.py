import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = (
    "data/raw/DHS/NGKR7BDT/NGKR7BFL.DTA"
)

def load_data():

    df = pd.read_stata(INPUT_PATH)

    assert df.shape[0] > 0

    logging.info(
        f"Loaded dataset with shape {df.shape}"
    )

    return df

def profile_dataset(df):

    print("\n")
    print("=" * 50)
    print("DATASET SHAPE")
    print("=" * 50)

    print(df.shape)

    print("\n")
    print("=" * 50)
    print("VARIABLE NAMES")
    print("=" * 50)

    print(df.columns.tolist())

    print("\n")
    print("=" * 50)
    print("DATA TYPES")
    print("=" * 50)

    print(df[["v190", "v106", "v012", "b19", "v025", "hw70"]].dtypes)

    print("\n")
    print("=" * 50)
    print("HW70 SAMPLE VALUES")
    print("=" * 50)

    print(df["hw70"].head(20))

    print("\n")
    print("=" * 50)
    print("MISSING VALUES")
    print("=" * 50)

    missing = df.isna().sum()

    print(missing.sort_values(ascending = False).head(20))

    study_vars = [
        "hw70",
        "v190",
        "v106",
        "b19",
        "v012",
        "v025"
    ]

    print("\n")
    print("=" * 50)
    print("MISSING VALUES IN STUDY VARIABLES")
    print("=" * 50)

    print(df[study_vars].isnull().sum())

    print("\n")
    print("=" * 50)
    print("DUPLICATE RECORDS")
    print("=" * 50)

    duplicates = df.duplicated().sum()

    print(f"Duplicate rows: {duplicates}")

def main():

    df = load_data()
    profile_dataset(df)

if __name__ == "__main__":
    main()

