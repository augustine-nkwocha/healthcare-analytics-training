import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

DB_PATH = (
    "data/interim/sqlite/week3_indicators.db"
)

def load_trend_data():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        ParentLocation,
        Period,
        AVG(FactValueNumeric)
            AS average_life_expectancy
    FROM life_expectancy
    WHERE Indicator = 
        'Life expectancy at birth (years)'
    AND Dim1 = 
        'Both sexes'
    GROUP BY 
        ParentLocation,
        Period
    ORDER BY
        ParentLocation,
        Period
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    logging.info(
        f"Loaded trend data with shape {df.shape}"
    )

    return df

def create_trend_plot(df):

    plt.figure(
        figsize=(12,7)
    )

    for region in (
        df["ParentLocation"]
        .unique()
    ):
        region_df = (
            df[
                df["ParentLocation"]
                == region
            ]
        )

        plt.plot(
            region_df["Period"],
            region_df[
                "average_life_expectancy"
            ],
            label = region
        )

    plt.xlabel("Year")
    plt.ylabel(
        "Average Life Expectancy"
    )

    plt.title(
        "Life Expectancy Trends by WHO Region (2000 - 2021)"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "figures/week3_life_expectancy_trends.png"
    )

    plt.show()

    logging.info(
        "Saved trend plot"
    )

def load_indicator_summary():

    return pd.read_csv(
        "reports/week3_indicator_summary.csv"
    )

def create_change_plot(df):

    plt.figure(
        figsize=(10,6)
    )

    plt.bar(
        df["WHO Region"],
        df["Absolute Change"]
    )

    plt.xticks(
        rotation=45
    )

    plt.ylabel(
        "Absolute Change (Years)"
    )

    plt.title(
        "Change in Life Expectancy (2000 - 2021)"
    )

    plt.tight_layout()

    plt.savefig(
        "figures/week3_aboslute_change.png"
    )

    plt.show()

    logging.info(
        "Saved change plot"
    )

def main():

    trend_df = (
        load_trend_data()
    )

    create_trend_plot(
        trend_df
    )

    summary_df = (
        load_indicator_summary()
    )

    create_change_plot(
        summary_df
    )

if __name__ == "__main__":
    main()


