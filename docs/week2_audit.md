# Week 2 Audit – COVID-19 Surveillance Analytics

## Dataset

WHO COVID-19 Global Daily Surveillance Dataset

## Scope of Analysis

Country: Nigeria

Analysis Period: 2020–2021

Reason for Selection:

- Reporting completeness was substantially better than later years.
- Daily case and death variables became increasingly incomplete after 2021.
- The selected period allowed meaningful surveillance analysis.


## Epidemiology Concepts Learned

### Surveillance Data

- Daily surveillance reporting
- Incident vs cumulative indicators
- Country-level surveillance monitoring

### Epidemic Curves

- Construction of epidemic curves
- Interpretation of epidemic waves
- Identification of wave peaks
- Identification of wave start and end periods

### Mortality Monitoring

- Cases vs deaths comparison
- Mortality burden assessment
- Deaths per 1,000 cases

### Analytical Reasoning

- Hypothesis generation
- Distinguishing findings from explanations
- Evaluating competing hypotheses
- Evidence-based interpretation


## Python and Pandas Skills Practiced

### Data Inspection

- shape
- columns
- dtypes
- head()

### Missingness Investigation

- isna()
- sum()
- percentage calculations
- grouping by year

### Filtering

- Country-specific subsets
- Time-period subsets
- Wave-specific subsets

### Aggregation

- groupby()
- monthly summaries
- wave summaries

### Time-Series Analysis

- datetime conversion
- date filtering
- moving averages
- monthly aggregation

### Visualization

- epidemic curves
- moving average plots
- dual-axis trend charts


## Findings Produced

### Data Quality

- Missingness increased substantially after 2021.
- Cumulative indicators were complete.
- Surveillance reporting quality varied over time.

### Epidemiologic Findings

Wave 1:

- Apr 2020 – Oct 2020
- Peak: Jul 2020

Wave 2:

- Dec 2020 – Apr 2021
- Peak: Jan 2021

Wave 3:

- Jul 2021 – Nov 2021
- Peak: Aug 2021

Wave 4:

- Emerging in Dec 2021
- Not fully observable within analysis period

### Wave Comparison

Wave 1:

- Cases: 62,555
- Deaths: 1,140
- Deaths per 1,000 cases: 18.22

Wave 2:

- Cases: 97,643
- Deaths: 890
- Deaths per 1,000 cases: 9.11

Wave 3:

- Cases: 42,279
- Deaths: 600
- Deaths per 1,000 cases: 14.19


## Deliverables Produced

- week2_covid_pipeline.py
- week2_dataset_profile.md
- week2_surveillance_report.md
- week2_stakeholder_summary.md
- week2_epi_curves.ipynb


## Portfolio Value

This project demonstrates:

- surveillance analytics
- epidemiologic reasoning
- time-series analysis
- public health reporting
- Git-based analytical workflow


## Gaps Remaining Before Week 3

Topics not yet covered:

- Incidence rates
- Prevalence
- Proportions
- Risk measures
- Stratified analysis
- Demographic subgroup analysis
- Comparative epidemiology
- Statistical inference

These will form the foundation of Week 3.