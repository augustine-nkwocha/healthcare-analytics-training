# Week 2 Dataset Profile

## Dataset

WHO COVID-19 Global Daily Surveillance Dataset

## Shape

- Rows: 556,560
- Columns: 8

## Unit of Observation

Each row represents one country on one reporting date.

## Variables

### Date Variable

- Date_reported

### Geographic Variables

- Country_code
- Country
- WHO_region

### Surveillance Indicators

- New_cases
- Cumulative_cases
- New_deaths
- Cumulative_deaths

## Data Types

| **Variable**      | **Type** |
|-------------------|----------|
| Date_reported     | str      |
| Country_code      | str      |
| Country           | str      |
| WHO_region        | str      |
| New_cases         | float64  |
| Cumulative_cases  | int64    |
| New_deaths        | float64  |
| Cumulative_deaths | int64    |

## Initial Observations

- Date_reported should be converted to datetime.
- Dataset is suitable for time-series analysis.
- Dataset supports country-level and regional surveillance analysis.
- Cumulative indicators should generally increase over time.

- Date_reported was converted from string to datetime.
- Missingness in New_cases and New_deaths increases substantially after 2023.
- Cumulative indicators have no missing values.
- Missingness patterns suggest possible changes in reporting practices over time.
- Further investigation is required before imputing or removing missing values.

- 46 cumulative case decreases were detected.
- These represent approximately 0.008% of all records.
- Most cumulative counts behave as expected.
- Several large retrospective corrections were identified.
- The largest observed correction was -65,079 cases in the Philippines on 2023-08-14.
- Large cumulative decreases should be investigated before trend analysis.

## Surveillance Reporting Findings

- Nigeria had relatively complete New_cases reporting in 2020–2021.
- Reporting completeness declined substantially in 2022.
- Daily case reporting became largely unavailable from 2023 onward.
- Daily death reporting became almost completely unavailable from 2023 onward.
- 2020–2021 are the most suitable years for epidemic curve analysis using Nigeria's reported incident counts.


## Lessons Learned

- Surveillance data quality must be assessed before analysis.
- Missingness patterns can determine whether a dataset is fit for a specific question.
- Epidemic curves help identify outbreak waves and peaks.
- Moving averages reduce daily reporting noise.
- Visual patterns should be verified with quantitative summaries.
- Case burden and mortality burden may differ substantially.
- Findings should be distinguished from hypotheses.
- All analyses should include limitations.