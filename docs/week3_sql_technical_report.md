# Week 3B Technical Report

## Objective
To investigate trends in life expectancy at birth across WHO regions between 2000 and 2021 using SQL and Python.

## Dataset

Source: WHO Global Health Observatory (GHO)

Rows: 24,420

Columns: 34

Analysis dataset: 24,420 rows and 7 columns.

## Research Questions

1. How has life expectancy at birth changed across WHO regions between 2000 and 2021?

2. Which regions experienced the greatest improvements?

3. How did life expectancy trends change around the COVID-19 period?

## Analytical Approach

- Dataset inspection and profiling.
- Creation of analysis dataset.
- Import into SQLite database.
- SQL aggregation queries.
- Construction of indicator summary table.
- Visualization of trends and changes.

## Key Results

- Africa experienced the largest increase in life expectancy (+9.28 years).
- South-East Asia experienced the second largest increase (+6.48 years).
- The Americas experienced the smallest increase (+0.23 years).
- Most regions experienced declines between 2019 and 2021.

## Limitations

- Regional averages may mask country-level heterogeneity.
- Causes of mortality were not analysed.
- Observational analysis cannot establish causality.

## Reproducibility

All scripts, SQL queries, reports, and figures have been saved in this repository.