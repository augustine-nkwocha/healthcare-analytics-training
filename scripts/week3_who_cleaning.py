import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = (
    "data/raw/who_gho_life_expectancy.csv"
)

OUTPUT_PATH = (
    "data/interim/who_gho_life_expectancy_analysis.csv"
)

def load_data():

    df = pd.read_csv(INPUT_PATH)

    assert df.shape[0] > 0

    logging.info(
        f"Loaded dataset with shape {df.shape}"
    )

    return df

def select_variables(df):

    analysis_df = df[
        [
            "Indicator",
            "ParentLocation",
            "Location",
            "Period",
            "Dim1",
            "FactValueNumeric",
            "Value"
        ]
    ].copy()

    logging.info(
        f"Created analysis dataset with shape {analysis_df.shape}"
    )

    return analysis_df

def inspect_analysis_dataset(
        analysis_df
):
    
    print("\n")
    print("=" * 50)
    print("ANALYSIS DATASET SHAPE")
    print("=" * 50)
    print(analysis_df.shape)

    print("\n")
    print("=" * 50)
    print("MISSINGNESS")
    print("=" * 50)
    print(
        analysis_df
        .isna()
        .sum()
    )

def save_dataset(
        analysis_df
):
    
    analysis_df.to_csv(
        OUTPUT_PATH,
        index = False
    )

    logging.info(
        f"Saved dataset to {OUTPUT_PATH}"
    )

def main():

    df = load_data()

    analysis_df = (
        select_variables(df)
    )

    inspect_analysis_dataset(
        analysis_df
    )

    save_dataset(
        analysis_df
    )

if __name__ == "__main__":
    main()
