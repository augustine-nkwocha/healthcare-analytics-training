import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:%(message)s"
)

INPUT_PATH = "data/interim/brfss_diabetes_analysis.csv"

def load_clean_dataset():
    df = pd.read_csv(INPUT_PATH)

    assert df.shape[0] > 0

    assert "diabetes_status" in df.columns

    logging.info(
        f"Loaded dataset with shape {df.shape}"
    )

    return df

def calculate_overall_prevalence(df):
    diabetes_counts = (
        df["diabetes_status"]
        .value_counts(dropna = False)
    )

    diabetes_percent = (
        df["diabetes_status"]
        .value_counts(
            normalize = True,
            dropna = True
        )
        * 100
    ).round(2)

    print("\n")
    print("=" * 50)
    print("OVERALL PREVALENCE")
    print("=" * 50)

    print(diabetes_counts)

    print(diabetes_percent)

    logging.info(
        "Calculated overall prevalence"
    )

    return diabetes_percent


def analyze_factor(
        df,
        factor_column,
        factor_name
):
    result = (
        pd.crosstab(
            df[factor_column],
            df["diabetes_status"],
            normalize = "index"
        )
        * 100
    ).round(2)

    print("\n")
    print("=" * 50)
    print(factor_name.upper())
    print("=" * 50)

    print(result)

    logging.info(
        f"Completed {factor_name}"
    )

    return result


def build_results_summary():
    results_summary = pd.DataFrame({
        "Factor": [
            "Sex",
            "Age",
            "BMI",
            "Smoking",
            "Exercise"
        ],

        "Lowest Group": [
            "Female",
            "18-24",
            "Underweight",
            "Some-Day Smoker",
            "Physically Active"
        ],

        "Lowest Prevalence (%)": [
            13.14,
            1.37,
            5.88,
            12.17,
            11.00
        ],

        "Highest Group": [
            "Male",
            "75-79",
            "Obese",
            "Former Smoker",
            "Not Physically Active"
        ],

        "Highest Prevalence (%)": [
            14.49,
            23.44,
            22.37,
            17.37,
            22.52
        ]
    })

    results_summary["Difference"] = (
        results_summary["Highest Prevalence (%)"]
        -
        results_summary["Lowest Prevalence (%)"]
    ).round(2)

    assert results_summary.shape[0] == 5

    logging.info(
        "Built results summary table"
    )

    return results_summary

def save_results_summary(
        results_summary
):
    
    results_summary.to_csv(
        "reports/week3_results_summary.csv",
        index=False
    )

    logging.info(
        "Saved results summary"
    )


def main():
    df = load_clean_dataset()

    calculate_overall_prevalence(df)
    
    sex_results = analyze_factor(
        df,
        "sex",
        "Sex Analysis"
    )

    age_results = analyze_factor(
        df,
        "age_group",
        "Age Analysis"
    )

    bmi_results = analyze_factor(
        df,
        "bmi_category",
        "BMI Analysis"
    )

    smoking_results = analyze_factor(
        df,
        "smoking_status",
        "Smoking Analysis"
    )

    exercise_results = analyze_factor(
        df,
        "exercise_status",
        "Exercise Analysis"
    )

    results_summary = (
        build_results_summary()
    )

    print("\n")
    print("=" * 50)
    print("RESULTS SUMMARY")
    print("=" * 50)
    print(results_summary)

    save_results_summary(
        results_summary
    )

if __name__ == "__main__":
    main()


