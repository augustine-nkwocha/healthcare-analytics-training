# Week 6 Study Protocol

Project: Association Between Cigarette Smoking and Diabetes Among US Adults Using NHANES 2017–March 2020 Pre-pandemic Data

Dataset: NHANES 2017–March 2020 Pre-pandemic

Study Design: Cross-sectional observational study

Created: 31 July 2026

Version: 1.0

---

# Study Protocol

## Purpose

This protocol describes the operational procedures that will be followed to conduct a reproducible epidemiological analysis of the association between cigarette smoking and diabetes among US adults using NHANES 2017–March 2020 Pre-pandemic data.

The objective is to ensure that every stage of the study is transparent, reproducible, and consistently executed.

---

## Data Source

The study will use publicly available NHANES 2017–March 2020 Pre-pandemic datasets released by the National Center for Health Statistics (NCHS).

Only datasets and variables required to answer the research question will be included in the analytical dataset.

---

## Study Population

The analytical population will consist of eligible adult participants represented in NHANES.

Final inclusion and exclusion criteria will be confirmed after reviewing the dataset documentation and selected variables.

---

## Variables

The study will identify and document:

- Participant identifier
- Exposure variable(s)
- Outcome variable(s)
- Potential confounding variable(s)

The exact variable names, coding schemes, and definitions will be documented during Variable Discovery and recorded in the Variable Dictionary.

---

## Data Acquisition

The required NHANES files will be downloaded from the official NHANES website and stored in:
data/raw/

The integrity of each downloaded dataset will be verified before use.

---

## Dataset Understanding

Each dataset will be examined to determine:

- Number of observations
- Number of variables
- Variable names
- Data types
- Missing values
- Overall dataset structure

---

## Variable Discovery

Variables required to answer the research question will be identified using the official NHANES documentation.

Each selected variable will be reviewed for:

- Variable description
- Coding
- Missing-value codes
- Eligible participants
- Measurement units (where applicable)

---

## Analysis Dataset Construction

Only variables required for the study will be extracted.

Datasets will be merged using the participant identifier.

The merged analytical dataset will be reviewed before cleaning begins.

---

## Data Cleaning

Cleaning procedures may include:

- Variable renaming
- Data type correction
- Missing-value handling
- Category recoding
- Logical consistency checks

All transformations will be documented and reproducible.

---

## Data Validation

The cleaned dataset will be validated by checking:

- Duplicate participant identifiers
- Missingness
- Data types
- Variable ranges
- Logical consistency
- Summary statistics

Any issues identified during validation will be investigated before analysis.

---

## Statistical Analysis

The planned analyses include:

1. Descriptive statistics
2. Exploratory data analysis
3. Estimation of smoking prevalence
4. Estimation of diabetes prevalence
5. Assessment of the association between smoking and diabetes
6. Stratified analyses where appropriate
7. Adjustment for selected confounders where appropriate

The final analytical approach will depend on the variables available in the analytical dataset.

---

## Expected Outputs

The project is expected to produce:

- Dataset Profile
- Variable Dictionary
- Analysis-ready dataset
- Statistical tables
- Figures
- Technical Report
- Stakeholder Summary

---

## Reproducibility

All analyses will be performed using documented Python scripts.

Scripts will follow the project coding standard, including:

- Structured logging
- Input validation
- Assertions where appropriate
- Exception handling
- Modular functions
- Clear documentation

The project will be maintained under version control using Git.