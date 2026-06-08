# Week 1 Ebola QC Report

## Dataset Summary

Rows: 6611

Columns: 28

Dataset Type: Ebola Line-list

# QC Findings

## Missingness

## | Variable        | Missing Count | Missing Percent |
   | ---------------- ---------------  --------------- |
   | infection_date  |     2322      |     35.12%      |
   | hospital        |     1512      |     22.87%      |
   | outcome         |     1500      |     22.69%      |
   | date_of_outcome |     1068      |     16.15%      |

## Duplicates

Exact duplicate rows: 2

## Temporal Violations

| Issue                          | Count | Percent |
|--------------------------------|-------|---------|
| Outcome before hospitalization | 224   | 3.39%   |

## Invalid Admission Times

| Issue                         | Count | Percent |
|-------------------------------|-------|---------|
| Invalid time_admission values | 53    | 0.80%   |

## Preliminary Risk Assessment

High risk: Missing infection dates

Moderate risk: Outcome before hospitalization

Low risk: Invalid admission times