# Healthcare Analytics Training

This repository contains my structured training projects in public health, epidemiology, clinical data management, and healthcare analytics.

The goal is to develop practical skills in:
- Data governance
- Epidemiological analysis
- Data cleaning and quality control
- Surveillance analytics
- SQL and health indicators
- Clinical data management
- Reproducible analytics workflows
- Data visualization and reporting



# Week 1 Project: Ebola Line-list Data Quality Assessment

## Dataset

WHO Ebola line-list dataset

- Records: 6,611
- Variables: 28


## Objectives

The objective of Week 1 was to:

- Understand the dataset structure
- Profile variables and data types
- Assess missingness
- Detect duplicate records
- Standardize column names
- Convert date variables
- Perform temporal quality checks
- Validate admission-time values
- Produce technical and stakeholder reports


## Workflow

Raw Dataset

data/raw/linelist_raw.csv

↓

Quality Control Pipeline

scripts/week1_ebola_qc.py

↓

Cleaned Dataset

data/interim/linelist_cleaned.csv

↓

Reports

reports/week1_qc_report.md

reports/week1_stakeholder_summary.md



# Key Findings

### Missingness

| Variable       | Missing Percent |
|----------------|-----------------|
| infection_date | 35.12%          |
| infector       | 35.14%          |
| source         | 35.14%          |
| hospital       | 22.87%          |
| outcome        | 22.69%          |

## Duplicate Records

- 2 exact duplicate rows identified

## Temporal Quality Issues

- 224 records had outcome dates occurring before hospitalization dates
- Represents 3.39% of all records

## Invalid Admission Times

Examples:

12:60

13:60

24:14

- 53 invalid records detected
- Represents 0.80% of all records



## Skills Demonstrated

- Python
- Pandas
- Data Quality Assessment
- Missing Data Analysis
- Temporal Validation
- Epidemiological Reasoning
- Git
- GitHub
- Technical Reporting
- Stakeholder Communication



## Project Structure

data/
├── raw/
├── interim/
└── processed/

docs/
├── governance_notes.md
├── sop_health_data_workflow.md
└── week1_dataset_profile.md

scripts/
└── week1_ebola_qc.py

reports/
├── week1_qc_report.md
└── week1_stakeholder_summary.md

tests/

notebooks/



## Status

Week 1 completed.

Next phase:
COVID surveillance analytics, dataset merging, epidemic curves, reporting-lag analysis, and automated pipelines.