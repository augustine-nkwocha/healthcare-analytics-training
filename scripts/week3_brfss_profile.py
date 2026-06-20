import pandas as pd

RAW_PATH = "data/raw/LLCP2022.XPT"
VARIABLE_LIST_PATH = "data/interim/brfss_variables.csv"

df = pd.read_sas(RAW_PATH)

print("\n")
print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n")
print("=" * 50)
print("FIRST 20 COLUMNS")
print("=" * 50)
print(df.columns[:20].tolist())

print("\n")
print("=" * 50)
print("LAST 30 COLUMNS")
print("=" * 50)
print(df.columns[-30:].tolist())

variables = pd.DataFrame({
    "variable": df.columns
})

variables.to_csv(
    VARIABLE_LIST_PATH,
    index=False
)

print("\n")
print("=" * 50)
print("VARIABLE LIST SAVED")
print("=" * 50)
print(VARIABLE_LIST_PATH)

candidate_vars = variables[
    variables["variable"].str.contains(
        "DIAB|AGE|BMI|SMOK|DRINK|EXER",
        case=False,
        na=False
    )
]

print("\n")
print("=" * 50)
print("CANDIDATE HEALTH VARIABLES")
print("=" * 50)
print(candidate_vars.to_string())

sex_vars = variables[
    variables["variable"].str.contains(
        "SEX",
        case=False,
        na=False
    )
]

print("\n")
print("=" * 50)
print("SEX-RELATED VARIABLES")
print("=" * 50)
print(sex_vars.to_string())

variables_of_interest = [
    "DIABETE4",
    "_AGEG5YR",
    "_BMI5CAT",
    "_SMOKER3",
    "EXERANY2",
    "SEXVAR",
    "_SEX"
]

print("\n")
print("=" * 50)
print("SELECTED VARIABLE VALUE COUNTS")
print("=" * 50)

for var in variables_of_interest:
    print("\n")
    print("=" * 50)
    print(var)
    print("=" * 50)
    print(df[var].value_counts(dropna=False))