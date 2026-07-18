# Week 4 Dataset Profile

## Dataset

Nigeria DHS 2018 KR Dataset

### 1. Dataset Dimensions

- Rows: 33,924
- Columns: 1,166

### Interpretation

- The dataset contains 33,924 observations.
- Each observation represents one child recorded in the Nigeria DHS 2018 Kids Recode (KR) dataset.
- The dataset contains 1,166 variables describing the child, mother, household, health, nutrition, vaccination, antropometry, and other characteristics.

### 2. Variable Names

Study variables
- v190
- v106
- v012
- b19
- v025
- hw70

### 3. Data Types

Data types of discovered variables

| **Variable** | **DataType** |
|--------------|--------------|
| v190         | category     |
| v106         | category     |
| v012         | int8         |
| b19          | int8         |
| v025         | category     |
| hw70         | category     |

### Observation

| **Variable** | **Expected**      | **Observed**         | **Note**                                                                        |
|--------------|-------------------|----------------------|---------------------------------------------------------------------------------|
| hw70         | Numeric HAZ score | Imported as category | Contains numeric values plus "flagged cases"; requires cleaning before analysis |

### 4. Missing Values

Study variables missingness

| **Variable** | **Missing** | **Action**                                                                                                 |
|--------------|-------------|------------------------------------------------------------------------------------------------------------|
| hw70         | 22,453      | Investigate why HAZ is missing and restrict the analysis to children with valid anthropometric measurements before analysis. |
| v190         | 0           | No action needed                                                                                           |
| v106         | 0           | No action needed                                                                                           |
| v012         | 0           | No action needed                                                                                           |
| b19          | 0           | No action needed                                                                                           |
| v025         | 0           | No action needed                                                                                           |

### 5. Duplicates

Duplicate rows = 0

### Interpretation
No completely duplicated records were identified in the KR dataset.

## Dataset Profiling Summary

### Key findings

- The KR dataset contains 33,924 child-level observations and 1,166 variables.
- All study variables required for the research question are available.
- Most study variables have no missing values.
- The outcome variable (hw70) contains substantial missing values that require investigation during the data cleaning stage.
- No completely duplicated records were found.

