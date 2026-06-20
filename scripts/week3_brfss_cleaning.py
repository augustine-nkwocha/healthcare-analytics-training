import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

RAW_PATH = "data/raw/LLCP2022.XPT"
OUTPUT_PATH = "data/interim/brfss_diabetes_analysis.csv"


def load_data(path):
    df = pd.read_sas(path)
    logging.info(f"Loaded dataset with shape: {df.shape}")
    return df


def select_analysis_variables(df):
    selected = [
        "DIABETE4",
        "_AGEG5YR",
        "SEXVAR",
        "_BMI5CAT",
        "_SMOKER3",
        "EXERANY2"
    ]

    analysis_df = df[selected].copy()

    assert analysis_df.shape[1] == 6

    logging.info(f"Selected analysis dataset shape: {analysis_df.shape}")

    return analysis_df


def recode_diabetes(analysis_df):
    analysis_df["diabetes_status"] = (
        analysis_df["DIABETE4"]
        .map({
            1: "Diabetes",
            2: "No Diabetes",
            3: "No Diabetes",
            4: "No Diabetes"
        })
    )

    logging.info("Recoded diabetes_status")

    return analysis_df


def recode_age(analysis_df):
    analysis_df["_AGEG5YR"] = (
        analysis_df["_AGEG5YR"]
        .replace(14, pd.NA)
    )

    analysis_df["age_group"] = (
        analysis_df["_AGEG5YR"]
        .map({
            1: "18-24",
            2: "25-29",
            3: "30-34",
            4: "35-39",
            5: "40-44",
            6: "45-49",
            7: "50-54",
            8: "55-59",
            9: "60-64",
            10: "65-69",
            11: "70-74",
            12: "75-79",
            13: "80+"
        })
    )

    logging.info("Recoded age_group")

    return analysis_df


def recode_smoking(analysis_df):
    analysis_df["_SMOKER3"] = (
        analysis_df["_SMOKER3"]
        .replace(9, pd.NA)
    )

    analysis_df["smoking_status"] = (
        analysis_df["_SMOKER3"]
        .map({
            1: "Daily Smoker",
            2: "Some-Day Smoker",
            3: "Former Smoker",
            4: "Never Smoked"
        })
    )

    logging.info("Recoded smoking_status")

    return analysis_df


def recode_exercise(analysis_df):
    analysis_df["EXERANY2"] = (
        analysis_df["EXERANY2"]
        .replace([7, 9], pd.NA)
    )

    analysis_df["exercise_status"] = (
        analysis_df["EXERANY2"]
        .map({
            1: "Physically Active",
            2: "Not Physically Active"
        })
    )

    logging.info("Recoded exercise_status")

    return analysis_df


def recode_sex(analysis_df):
    analysis_df["sex"] = (
        analysis_df["SEXVAR"]
        .map({
            1: "Male",
            2: "Female"
        })
    )

    logging.info("Recoded sex")

    return analysis_df


def recode_bmi(analysis_df):
    analysis_df["bmi_category"] = (
        analysis_df["_BMI5CAT"]
        .map({
            1: "Underweight",
            2: "Normal Weight",
            3: "Overweight",
            4: "Obese"
        })
    )

    logging.info("Recoded bmi_category")

    return analysis_df


def assess_missingness(analysis_df):
    missing_summary = pd.DataFrame({
        "Missing Count": analysis_df.isna().sum(),
        "Missing Percent": (
            analysis_df.isna().sum()
            / len(analysis_df)
            * 100
        ).round(2)
    })

    print("\n")
    print("=" * 50)
    print("MISSINGNESS SUMMARY")
    print("=" * 50)
    print(missing_summary)

    return missing_summary


def validate_clean_dataset(analysis_df):
    expected_columns = [
        "DIABETE4",
        "_AGEG5YR",
        "SEXVAR",
        "_BMI5CAT",
        "_SMOKER3",
        "EXERANY2",
        "diabetes_status",
        "sex",
        "age_group",
        "bmi_category",
        "smoking_status",
        "exercise_status"
    ]

    assert list(analysis_df.columns) == expected_columns
    assert analysis_df.shape[1] == 12

    logging.info("Clean dataset validation passed")


def save_clean_dataset(analysis_df, path):
    analysis_df.to_csv(path, index=False)
    logging.info(f"Saved clean dataset to {path}")


def main():
    df = load_data(RAW_PATH)

    analysis_df = select_analysis_variables(df)

    analysis_df = recode_diabetes(analysis_df)
    analysis_df = recode_sex(analysis_df)
    analysis_df = recode_age(analysis_df)
    analysis_df = recode_bmi(analysis_df)
    analysis_df = recode_smoking(analysis_df)
    analysis_df = recode_exercise(analysis_df)

    assess_missingness(analysis_df)

    validate_clean_dataset(analysis_df)

    save_clean_dataset(analysis_df, OUTPUT_PATH)


if __name__ == "__main__":
    main()
