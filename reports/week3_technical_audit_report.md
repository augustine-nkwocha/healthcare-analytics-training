
# Week3: Diabetes Prevalence Analysis Using BRFSS 2022 Data

## Objective
To estimate diabetes prevalence and examine how prevalence varies according to demographic and behioral characteristics among respondents in the BRFSS 2022 survey.

## Dataset Information

### Dataset:
Behavioral Risk Factor Surveillance System (BRFSS) 2022

### Source:
CDC BRFSS Public Use Data

### Dataset Shape:
445,132 rows
328 columns

### Unit of Observation:
One survey respondent who participated in the BRFSS 2022 survey.

### Study Population:
Adult respondents who participated in the 2022 BRFSS survey.

## Variables  Selected

### outcome Variable

| **Source Variable** | **Analytical Variable** |
|---------------------|-------------------------|
| DIABETE4            | diabetes_status         |

### Predictor Variables

| **Source Variable** | **Analytical Variable** |
|---------------------|-------------------------|
| SEXVAR              | sex                     |
| _AGEG5YR            | age_group               |
| _BMI5CAT            | bmi_category            |
| _SMOKER3            | smoking_status          |
| EXERANY2            | exercise_status         |


## Recoding Decisions

### Diabetes

1 → Diabetes
2 → No Diabetes
3 → No Diabetes
4 → No Diabetes
7, 9 → Missing

### Age

1 → 18–24
2 → 25–29
...
13 → 80+
14 → Missing

### Smoking

9 → Missing

### Exercise

7, 9 → Missing

### BMI

Retained existing BMI categories from BRFSS.


## Missingness Assessment

| Variable | Missing Count | Missing Percent |
|----------|---------------|-----------------|
| DIABETE4 | 3             | 0.00            |
| _AGEG5YR | 9,079         | 2.04            |
| _BMI5CAT | 48,806        | 10.96           |
| _SMOKER3 | 35,462        | 7.97            |
| EXERANY2 | 1,093         | 0.25            |


## Analytical Decisions

Prevalence estimates were calculated using respondents with known diabetes status only.

Stratified prevalence analyses were performed for:
- Sex
- Age group
- BMI category
- Smoking status
- Physical activity status


## Key Findings

- Overall diabetes prevalence: 13.77%.
- Age demonstrated the largest crude difference in prevalence (22.07 percentage points).
- Obesity and physical inactivity were also strongly associated with diabetes prevalence.
- Differences by sex were comparatively small.


## Limitations

- Cross-sectional observational design.
- Self-reported survey responses.
- Potential confounding.
- Missing data in several variables.
- Associations should not be interpreted as causal relationships.


## Outputs Produced

scripts/
    week3_brfss_profile.py
    week3_brfss_cleaning.py
    week3_analysis.py

data/interim/
    brfss_variables.csv
    brfss_diabetes_analysis.csv

docs/
    week3_dataset_profile.md    

reports/
    week3_results_summary.csv
    week3_stakeholder_summary.md
    week3_technical_audit_report.md