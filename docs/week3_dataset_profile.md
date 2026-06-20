# Week 3 Dataset Profile – BRFSS 2022 Diabetes Analysis

## Dataset Information

Dataset Name:
Behavioral Risk Factor Surveillance System (BRFSS) 2022

Source:
Centers for Disease Control and Prevention (CDC)

File:
LLCP2022.XPT

Year:
2022

Dataset Type:
Cross-sectional population health survey


## Dataset Shape

Rows:
445,132

Columns:
328


## Unit of Observation

Each row represents one survey respondent who participated in the 2022 BRFSS survey.

## Purpose of Dataset

The BRFSS collects information on:

- Chronic diseases
- Health behaviors
- Preventive health practices
- Healthcare access
- Risk factors

among adults in the United States.


## Initial Analytical Objective

To investigate whether diabetes prevalence differs according to:

- Age
- Sex
- BMI category
- Smoking status
- Physical activity

## Candidate Outcome Variable

### DIABETE4

Description:

Ever told you had diabetes.

Possible Values:

- 1 = Yes
- 2 = Yes, only during pregnancy
- 3 = No
- 4 = Prediabetes
- 7 = Don’t know
- 9 = Refused
- Missing

Observed Counts:

- 1 = 61,158
- 2 = 3,836
- 3 = 368,722
- 4 = 10,329
- 7 = 763
- 9 = 321
- Missing = 3

Notes:

Contains special codes requiring recoding before analysis.


## Candidate Predictor Variables

### SEXVAR

Description:

Respondent sex

Observed Values:

- 1 = Male
- 2 = Female

Missing:
None observed.


### _AGEG5YR

Description:

Age grouped into 5-year categories.

Observed Values:

1–14 age groups.

Missing:
None observed.


### _BMI5CAT

Description:

BMI category.

Observed Values:

- 1 = Underweight
- 2 = Normal Weight
- 3 = Overweight
- 4 = Obese

Missing:
48,806

Approximate Missingness:
11%


### _SMOKER3

Description:

Smoking status.

Observed Values:

- 1 = Current smoker
- 2 = Current smoker some days
- 3 = Former smoker
- 4 = Never smoked
- 9 = Missing / Refused

Missing-like category:
35,462


### EXERANY2

Description:

Physical activity in past 30 days.

Observed Values:

- 1 = Yes
- 2 = No
- 7 = Don’t know
- 9 = Refused
- Missing

Missingness:
Very low.


### Data Types

Likely categorical variables selected for analysis:

- DIABETE4
- SEXVAR
- _AGEG5YR
- _BMI5CAT
- _SMOKER3
- EXERANY2


## Initial Data Quality Findings

1. DIABETE4 contains special response codes.
2. _BMI5CAT contains approximately 11% missing values.
3. _SMOKER3 contains refusal/missing category.
4. EXERANY2 contains very few unknown/refused responses.
5. SEXVAR and _AGEG5YR appear complete.


## Outcome Definition

Outcome Variable:
DIABETE4

Research Question:

Does diabetes prevalence differ according to age, sex, BMI category, smoking status, and physical activity?

Outcome Categories:

Diabetes:

- DIABETE4 = 1

No Diabetes:

- DIABETE4 = 2
- DIABETE4 = 3
- DIABETE4 = 4

Excluded:

- DIABETE4 = 7
- DIABETE4 = 9
- Missing

Justification:

The objective is to distinguish respondents with diabetes from respondents without diabetes. Gestational diabetes only, prediabetes, and no diabetes are classified as non-diabetes for this specific analysis. Respondents with unknown or refused responses are excluded.


## Planned Cleaning Actions

- Recode diabetes outcome.
- Handle refusal and unknown categories.
- Assess BMI missingness.
- Create clean analysis dataset.
- Document exclusions.

## Analytical Missingness

The dataset contains coded non-response categories that are not represented as NaN values.

_SMOKER3:
- 9 = Unknown/Refused
- Will be recoded to missing

EXERANY2:
- 7 = Don't know
- 9 = Refused
- Will be recoded to missing

These categories do not provide usable information for the planned analysis and will be treated as missing values.


## Missing Data Strategy

A complete-case approach will not be used.

Respondents with missing values in one predictor variable will be retained in the dataset whenever possible.

Rationale:

A respondent with missing BMI may still contribute valid information to analyses involving age, sex, smoking status, or physical activity.

Variable-specific exclusions will therefore be applied during analysis rather than removing respondents from the entire analysis dataset.

## Analysis Dataset Specification

Outcome:
- diabetes_status

Predictors:
- sex
- age_group
- bmi_category
- smoking_status
- exercise_status

Source variables retained for traceability:
- DIABETE4
- SEXVAR
- _AGEG5YR
- _BMI5CAT
- _SMOKER3
- EXERANY2

Analytical variables created:
- diabetes_status
- sex
- age_group
- bmi_category
- smoking_status
- exercise_status