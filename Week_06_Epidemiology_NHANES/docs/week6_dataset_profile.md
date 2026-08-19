# Week 6 Dataset Profile

Project: Association Between Cigarette Smoking and Diabetes Among US Adults Using NHANES 2017–March 2020 Pre-pandemic Data

Dataset: NHANES 2017–March 2020 Pre-pandemic

Created: 04 August 2026

Version: 1.0

---

# Dataset Profile

## Dataset Name

National Health and Nutrition Examination Survey (NHANES)
2017–March 2020 Pre-pandemic

---

## Data Source

National Center for Health Statistics (NCHS)

Centers for Disease Control and Prevention (CDC)

---

## Dataset Type

Nationally representative cross-sectional health survey.

---

## Purpose of the Dataset

NHANES is designed to assess the health and nutritional status of the civilian, non-institutionalized population of the United States.

The survey combines interviews, physical examinations and laboratory measurements to provide nationally representative health data.

---

## Study Design

Cross-sectional observational survey.

---

## Target Population

Civilian, non-institutionalized residents of the United States selected through the NHANES sampling design.

---

## Datasets Included in this Project

The current project will initially use:

- Demographics
- Body Measures
- Smoking Questionnaire
- Diabetes Questionnaire

Additional NHANES datasets may be incorporated later if required by the analysis.

---

## Unit of Observation

Each record represents one survey participant.

Participants are uniquely identified using the variable:

SEQN

---

## Data Format

SAS Transport (.xpt)

---

## Planned Data Integration

Datasets will be merged using the participant identifier (SEQN).

---

## Initial Dataset Summary

A detailed summary of the datasets will be generated using
week6_dataset_understanding.py.

The summary will include:

- Number of observations
- Number of variables
- Variable names
- Variable types
- Missing values
- Dataset dimensions

---

## Strengths

- Nationally representative sample.
- Standardized data collection procedures.
- Rich demographic, behavioural, examination and laboratory information.
- Widely used in epidemiological research.

---

## Limitations

- Cross-sectional design.
- Cannot establish causality.
- Some variables are self-reported.
- Missing data may be present.
- Some variables apply only to eligible participants.