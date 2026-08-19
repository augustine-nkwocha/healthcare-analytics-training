# Week 6 Variable Dictionary

**Project**: Association Between Cigarette Smoking and Diabetes Among US Adults Using NHANES 2017–March 2020 Pre-Pandemic Data

**Dataset**: NHANES 2017–March 2020 Pre-Pandemic

**Version**: 1.0



## Purpose
This variable dictionary documents the variables selected for the Week 6 analysis, their analytical roles, source datasets, meanings, coding, and planned treatment.
Only variables justified by the research question, study population, confounding strategy, data linkage requirements, or NHANES survey design are included.



## 1. Participant Identifier

### SEQN
**Source**: P_DEMO, P_SMQ, P_DIQ, P_BMX

**Role**: Participant identifier / linkage variable

**Meaning**: Respondent sequence number.

**Planned use**:

- Identify individual NHANES participants.
- Link records across the demographics, smoking, diabetes, and body-measures datasets.
- Check participant-level uniqueness before merging.

**Planned transformation**: None.



## 2. Eligibility and Age

### RIDAGEYR

**Source**: P_DEMO

**Role**: Eligibility variable and potential confounder

**Meaning**: Age in years at screening.

**Planned use**:
- Restrict the study population to adults aged 18 years or older.
- Retain age as a potential confounding variable.

**Initial analytical treatment**: Continuous age in years.

**Important note**: NHANES top-codes age at 80 years for participants aged 80 years and older.



## 3. Sex

### RIAGENDR

**Source**: P_DEMO

**Role**: Potential confounder

**Coding**:

- 1 = Male
- 2 = Female

**Planned use**: Assess and potentially adjust for confounding by sex.

**Planned transformation**: Recode numerical values to labelled categories for analysis and reporting.



## 4. Cigarette-Smoking History

### SMQ020

**Source**: P_SMQ

**Role**: Exposure-definition component

**Meaning**: Whether the participant has smoked at least 100 cigarettes during their lifetime.

**Target population**: Adults aged 18 years or older.

**Coding**:

- 1 = Yes
- 2 = No
- 7 = Refused
- 9 = Don’t know

**Planned use**: Used together with SMQ040 to derive cigarette-smoking status.

**Planned treatment**:

- 1 = Continue to SMQ040 for smoking-status classification.
- 2 = Never smoker.
- 7 and 9 = Treat as unknown/missing for the derived exposure.



## 5. Current Cigarette Smoking

### SMQ040

**Source**: P_SMQ

**Role**: Exposure-definition component

**Meaning**: Whether the participant currently smokes cigarettes.

**Coding**:

- 1 = Every day
- 2 = Some days
- 3 = Not at all
- 7 = Refused
- 9 = Don’t know

**Important skip-pattern note**:

SMQ040 is a follow-up question for participants whose preceding smoking history makes the question applicable. Therefore, missing SMQ040 values must not automatically be interpreted as ordinary missing data.

**Planned use with SMQ020**:

- SMQ020 = 2 → Never smoker
- SMQ020 = 1 and SMQ040 = 3 → Former smoker
- SMQ020 = 1 and SMQ040 = 1 or 2 → Current smoker
- Refused / Don’t know / otherwise unresolved → Missing or unknown smoking status

**Derived variable planned**: smoking_status

**Derived categories**:

- Never
- Former
- Current



## 6. Diabetes Status

### DIQ010

**Source**: P_DIQ

**Role**: Primary outcome

**Meaning**: Whether the participant has ever been told by a doctor or health professional that they have diabetes or sugar diabetes, excluding diabetes during pregnancy where applicable.

**Coding**:

- 1 = Yes
- 2 = No
- 3 = Borderline
- 7 = Refused
- 9 = Don’t know

**Primary outcome definition**:

- 1 → Diabetes
- 2 → No diabetes
- 3 → Borderline; not automatically classified as diabetes or no diabetes
- 7 / 9 → Missing or unknown

**Derived variable planned**: diabetes_status

**Important interpretation note**:

This variable represents self-reported health-professional-diagnosed diabetes. It should not be described as laboratory-confirmed diabetes or total biological diabetes prevalence.



## 7. Body Mass Index

### BMXBMI

**Source**: P_BMX

**Role**: Potential confounder

**Meaning**: Body mass index calculated from measured weight and height.

**Unit**: kg/m²

**Planned analytical treatment**: Initially retain as a continuous variable.

**Missing values**: To be assessed after constructing the eligible research dataset.

**Important measurement note**:

BMI is based on measurements collected during the Mobile Examination Center examination rather than participant self-report.



## 8. MEC Examination Weight

### WTMECPRP

**Source**: P_DEMO

**Role**: Survey weight

**Purpose**: Provide the appropriate full-sample examination weight for analysis of the combined NHANES 2017–March 2020 pre-pandemic release when examination data are incorporated.

**Planned use**: Survey-weighted estimation where required.

**Important note**: The project incorporates body-measures examination data; therefore, survey weighting must account for the examination component rather than treating the analytical sample as a simple random sample.



## 9. Survey Primary Sampling Unit

### SDMVPSU

**Source**: P_DEMO

**Role**: Complex survey-design variable

**Meaning**: Masked variance pseudo-primary sampling unit.

**Planned use**: Account for NHANES clustering when conducting survey-aware statistical analyses.



## 10. Survey Stratum

### SDMVSTRA

**Source**: P_DEMO

**Role**: Complex survey-design variable

**Meaning**: Masked variance pseudo-stratum.

**Planned use**: Account for NHANES stratification when conducting survey-aware statistical analyses.



## Planned Derived Variables

### smoking_status

Derived from:
- SMQ020
- SMQ040

Categories:
- Never
- Former
- Current



## diabetes_status

Derived primarily from DIQ010.

Primary binary comparison:
- Diabetes
- No diabetes

Borderline and unresolved responses will be handled explicitly rather than silently assigned to either category.


## Initial Research Variable Set

The research dataset will initially contain:
- SEQN
- RIDAGEYR
- RIAGENDR
- SMQ020
- SMQ040
- DIQ010
- BMXBMI
- WTMECPRP
- SDMVPSU
- SDMVSTRA

Derived variables will subsequently include:
- smoking_status
- diabetes_status


## Traceability to Research Question

**Exposure**: Cigarette-smoking status
→ SMQ020 + SMQ040

**Outcome**: Diabetes status
→ DIQ010

**Population**: US adults represented in the selected NHANES release
→ RIDAGEYR ≥ 18

**Potential confounders**:
→ RIDAGEYR
→ RIAGENDR
→ BMXBMI

**Participant linkage**:
→ SEQN

**Complex survey design**:
→ WTMECPRP
→ SDMVPSU
→ SDMVSTRA

