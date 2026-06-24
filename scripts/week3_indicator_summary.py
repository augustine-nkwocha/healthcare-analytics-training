import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

indicator_summary = pd.DataFrame({
    "WHO Region": [
        "Africa",
        "Americas",
        "Eastern Mediterranean",
        "Europe",
        "South-East Asia",
        "Western Pacific"
    ],

    "Life Expectancy 2000": [
        54.23,
        72.65,
        68.53,
        73.66,
        65.70,
        69.31
    ],

    "Life Expectancy 2021": [
        63.51,
        72.88,
        71.12,
        76.93,
        72.18,
        72.37
    ]
})

indicator_summary["Absolute Change"] = (
    indicator_summary["Life Expectancy 2021"]
    -
    indicator_summary["Life Expectancy 2000"]
).round(2)

print(indicator_summary)

indicator_summary.to_csv(
    "reports/week3_indicator_summary.csv",
    index = False
)

logging.info(
    "Indicator summary saved."
)

