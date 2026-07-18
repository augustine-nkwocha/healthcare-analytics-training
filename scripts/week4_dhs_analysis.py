import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = (
    "data/processed/week4_dhs_cleaned.csv"
)

OUTPUT_PATH = (
    "reports/week4_indicator_summary.csv"
)

def load_clean_data():

    df = pd.read_csv(INPUT_PATH)

    assert df.shape[0] > 0

    logging.info(
        f"Loaded cleaned dataset with shape {df.shape}"
    )

    return df

def describe_dataset(df):

    print("\n")
    print("=" * 50)
    print("ANALYSIS DATASET SHAPE")
    print("=" * 50)

    print(df.shape)

    print("\n")
    print("=" * 50)
    print("ANALYSIS DATASET COLUMNS")
    print("=" * 50)

    print(df.columns.tolist())

    assert "stunted" in df.columns
    assert "v190" in df.columns

    logging.info(
        "Analysis dataset described successfully"
    )

def overall_stunting_prevalence(df):

    print("\n")
    print("=" * 50)
    print("OVERALL STUNTING PREVALENCE")
    print("=" * 50)

    analysis_df = (
        df
        .dropna(subset = ["stunted"])
        .copy()
    )

    total_children = len(analysis_df)
    stunted_children = analysis_df["stunted"].sum()
    prevalence = (
        stunted_children
        /
        total_children
    ) * 100

    print(f"Total valid children: {total_children}")
    print(f"Stunted children: {stunted_children}")
    print(f"Stunting prevalence: {prevalence:.2f}%")

    assert total_children > 0
    assert stunted_children >= 0
    assert prevalence >= 0

    logging.info(
        "Overall stunting prevalence calculated successfully"
    )


def stunting_by_wealth(df):

    print("\n")
    print("=" * 50)
    print("STUNTING BY HOUSEHOLD WEALTH")
    print("=" * 50)

    analysis_df =(
        df
        .dropna(subset = ["stunted"])
        .copy()
    )

    wealth_summary = (
        analysis_df
        .groupby("v190", observed = True)["stunted"]
        .agg(
            Total_Children = "count",
            Stunted_Children = "sum"
        )
        .reset_index()
    )

    wealth_summary["Stunting_Prevalence"] = (
        wealth_summary["Stunted_Children"]
        / wealth_summary["Total_Children"]
        * 100
    )

    print(wealth_summary)

    assert wealth_summary.shape[0] > 0
    assert wealth_summary["Total_Children"].sum() == len(analysis_df)

    logging.info(
        "Stunting by household wealth calculated successfully."
    )

    return wealth_summary

def summary_statistics(df):

    print("\n")
    print("=" * 50)
    print("SUMMARY STATISTICS")
    print("=" * 50)

    analysis_df = (
        df
        .dropna(subset = ["hw70"])
        .copy()
    )

    summary = (
        analysis_df[
            ["hw70", "v012", "b19"]
        ]
        .describe()
        .round(2)
    )

    print(summary)

    assert summary.shape[1] == 3

    logging.info(
        "Summary statistics generated successfully "
    )
def save_indicator_summary(wealth_summary):

    wealth_summary.to_csv(
        OUTPUT_PATH,
        index = False
    )

    assert OUTPUT_PATH.endswith(".csv")

    logging.info(
        f"Saved indicator summary to {OUTPUT_PATH}"
    )

def main():

    df = load_clean_data()

    describe_dataset(df)

    overall_stunting_prevalence(df)

    wealth_summary = stunting_by_wealth(df)

    summary_statistics(df)

    save_indicator_summary(wealth_summary)

if __name__ == "__main__":

    main()

