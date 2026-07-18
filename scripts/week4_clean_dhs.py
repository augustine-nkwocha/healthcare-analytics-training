import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = (
    "data/interim/week4_dhs_research_dataset.csv"
)

OUTPUT_PATH = (
    "data/processed/week4_dhs_cleaned.csv"
)

def load_research_dataset():

    df = pd.read_csv(INPUT_PATH)

    assert df.shape[0] > 0

    logging.info(
        f"Loaded research dataset with shape {df.shape}"
    )

    return df

def inspect_research_dataset(df):

    print("\n")
    print("=" * 50)
    print("RESEARCH DATASET SHAPE")
    print("=" * 50)

    print(df.shape)

    print("\n")
    print("=" * 50)
    print("DATA TYPES")
    print("=" * 50)

    print(df.dtypes)

    print("\n")
    print("=" * 50)
    print("MISSING VALUES")
    print("=" * 50)

    print(df.isna().sum())

    print("\n")
    print("=" * 50)
    print("HW70 VALUE COUNTS")
    print("=" * 50)

    print(df["hw70"].value_counts(dropna = False).head(20))

def clean_hw70(df):

    print("\n")
    print("=" * 50)
    print("CLEANING HW70")
    print("=" * 50)

    # Replace flagged cases with missing values
    df["hw70"] = (
        df["hw70"]
        .replace("flagged cases", pd.NA)
    )

    # Convert to numeric
    df["hw70"] = pd.to_numeric(
        df["hw70"],
        errors = "coerce"
    )

    # Convert DHS scaled values to actual HAZ scores
    df["hw70"] = df["hw70"] / 100

    # Validation
    assert df["hw70"].dtype == "float64"
    assert "flagged cases" not in df["hw70"].astype(str).values

    logging.info(
        "HW70 cleaned successfully."
    )

    return df

def clean_v190(df):

    print("\n")
    print("=" * 50)
    print("CLEANING V190")
    print("=" * 50)

    # Validation before cleaning
    assert "v190" in df.columns

    # Convert to category
    df["v190"] = df["v190"].astype("category")

    # Validation after cleaning
    assert str(df["v190"].dtype) == "category"
    assert df["v190"].isna().sum() == 0

    logging.info(
        "V190 Cleaned successfully"
    )

    return df

def clean_v106(df):

    print("\n")
    print("=" * 50)
    print("CLEANING V106")
    print("=" * 50)

    # Validation before cleaning
    assert "v106" in df.columns

    # Convert to category
    df["v106"] = df["v106"].astype("category")

    # Validation
    assert str(df["v106"].dtype) == "category"
    assert df["v106"].isna().sum() == 0

    logging.info(
        "V106 cleaned successfully"
    )

    return df

def clean_v025(df):

    print("\n")
    print("=" * 50)
    print("CLEANING V025")
    print("=" * 50)

    # Validation before cleaning
    assert "v025" in df.columns

    # Convert to category
    df["v025"] = df["v025"].astype("category")

    # Validation
    assert str(df["v025"].dtype) == "category"
    assert df["v025"].isna().sum() == 0

    logging.info(
        "V025 cleaned successfully"
    )

    return df

def clean_v012(df):

    print("\n")
    print("=" * 50)
    print("CLEANING V012")
    print("=" * 50)

    # Validation
    assert "v012" in df.columns
    assert str(df["v012"].dtype) == "int64"
    assert df["v012"].isna().sum() == 0

    logging.info(
        "V012 cleaned successfully."
    )

    return df

def clean_b19(df):

    print("\n")
    print("=" * 50)
    print("CLEANING B19")
    print("=" * 50)

    # Validation
    assert "b19" in df.columns
    assert str(df["b19"].dtype) == "int64"
    assert df["b19"].isna().sum() == 0

    logging.info(
        "B19 cleaned successfully."
    )

    return df

def create_stunting_variable(df):

    print("\n")
    print("=" * 50)
    print("CREATING STUNTING VARIABLE")
    print("=" * 50)

    df["stunted"] = (
        df["hw70"] < -2
    ).astype("boolean")

    # Keep missing HAZ as missing stunting status
    df.loc[
        df["hw70"].isna(),
        "stunted"
    ] = pd.NA

    # Validation
    assert "stunted" in df.columns
    assert str(df["stunted"].dtype) == "boolean"

    logging.info(
        "Stunting variable created successfully."
    )

    return df

def validate_cleaned_dataset(df):

    print("\n")
    print("=" * 50)
    print("VALIDATING CLEANED DATASET")
    print("=" * 50)

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nMISSING VALUES")
    print(df.isna().sum())

    print("\nSTUNTING COUNTS")
    print(
        df["stunted"]
        .value_counts(dropna = False)
    )

    assert str(df["hw70"].dtypes) == "float64"
    assert str(df["v190"].dtypes) == "category"
    assert str(df["v106"].dtypes) == "category"
    assert str(df["v025"].dtypes) == "category"
    assert str(df["v012"].dtypes) == "int64"
    assert str(df["b19"].dtypes) == "int64"
    assert str(df["stunted"].dtypes) == "boolean"

    assert "flagged cases" not in df["hw70"].astype(str).values

    logging.info(
        "Cleaned dataset validation completed successfully"
    )

def save_cleaned_dataset(df):

    df.to_csv(
        OUTPUT_PATH,
        index = False
    )

    logging.info(
        f"Saved cleaned dataset to {OUTPUT_PATH}"
    )


def main():

    df = load_research_dataset()

    inspect_research_dataset(df)

    df = clean_hw70(df)

    df = clean_v190(df)

    df = clean_v106(df)

    df = clean_v025(df)

    df = clean_v012(df)

    df = clean_b19(df)

    df = create_stunting_variable(df)

    validate_cleaned_dataset(df)

    save_cleaned_dataset(df)
    


if __name__ == "__main__":

    main()
    
