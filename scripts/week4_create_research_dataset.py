import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = (
    "data/raw/DHS/NGKR7BDT/NGKR7BFL.DTA"
)

OUTPUT_PATH = (
    "data/interim/week4_dhs_research_dataset.csv"
)

def load_data():

    df = pd.read_stata(INPUT_PATH)

    assert df.shape[0] > 0

    logging.info(
        f"Loaded dataset with shape {df.shape}"
    )

    return df

def create_research_dataset(df):

    study_variables = [
        "hw70",
        "v190",
        "v106",
        "v012",
        "b19",
        "v025"
    ]

    research_df = (
        df[study_variables]
        .copy()
    )

    print("\n")
    print("=" * 50)
    print("RESEARCH DATASET SHAPE")
    print("=" * 50)

    print(research_df.shape)

    return research_df

def save_research_dataset(research_df):

    research_df.to_csv(
        OUTPUT_PATH,
        index = False
    )

    logging.info(
        f"Saved research dataset to {OUTPUT_PATH}"
    )

def main():

    df = load_data()

    research_df = create_research_dataset(df)

    save_research_dataset(research_df)

if __name__ == "__main__":

    main()

