import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = (
    "reports/week4_indicator_summary.csv"
)

OUTPUT_PATH = (
    "figures/week4_stunting_by_wealth.png"
)

OUTPUT_PATH_HAZ = (
    "figures/week4_haz_distribution.png"
)

CLEAN_DATA_PATH = (
    "data/processed/week4_dhs_cleaned.csv"
)

def load_indicator_summary():

    df = pd.read_csv(INPUT_PATH)

    assert df.shape[0] > 0

    logging.info(
        f"Loaded indicator summary with shape {df.shape}"
    )

    return df

def plot_stunting_by_wealth(df):

    wealth_order = [
        "poorest",
        "poorer",
        "middle",
        "richer",
        "richest"
    ]

    df["v190"] = pd.Categorical(
        df["v190"],
        categories = wealth_order,
        ordered = True
    )

    df = df.sort_values("v190")

    plt.figure(figsize = (8, 5))

    plt.bar(
        df["v190"],
        df["Stunting_Prevalence"]
    )

    plt.title(
        "Stunting Prevalence by Household Wealth"
    )

    plt.xlabel("Household Wealth Quintile")
    plt.ylabel("Stunting Prevalence (%)")

    plt.tight_layout()

    plt.savefig(OUTPUT_PATH)

    plt.close()

    logging.info(
        f"Figure saved to {OUTPUT_PATH}"
    )

def load_clean_dataset():

    df = pd.read_csv(CLEAN_DATA_PATH)

    assert df.shape[0] > 0

    logging.info(
        f"Loaded cleaned dataset with shape {df.shape}"
    )

    return df

def plot_haz_distribution(df):

    analysis_df = (
        df
        .dropna(subset = ["hw70"])
        .copy()
    )

    plt.figure(figsize = (8,5))

    plt.hist(
        analysis_df["hw70"],
        bins = 30
    )

    plt.title(
        "Distribution of Height-for-Age Z-score"
    )

    plt.xlabel(
        "Height-for-Age Z-score (HAZ)"
    )

    plt.ylabel(
        "Number of Children"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH_HAZ
    )

    plt.close()

    logging.info(
        f"Figure saved to {OUTPUT_PATH_HAZ}"
    )


def main():

    indicator_df = load_indicator_summary()

    plot_stunting_by_wealth(indicator_df)

    clean_df = load_clean_dataset()

    plot_haz_distribution(clean_df)
    

if __name__  == "__main__":

    main()  
