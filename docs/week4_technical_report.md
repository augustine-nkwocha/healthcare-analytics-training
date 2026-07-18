# Technical Report

## 1. Background

Childhood stunting is a major public health concern because it reflects chronic undernutrition during the critical periods of growth and development. Stunting is associated with impaired physical growth, reduced cognitive development, poorer educational outcomes, lower productivity in adulthood, and increased susceptibility to disease. Understanding factors associated with childhood stunting is essential for designing effective public health interventions and allocating resources to populations at greatest risk.



## 2. Research Question

Is household wealth associated with childhood stunting among children under five years of age in Nigeria?



## 3. Objectives

The objectives of this study were to:

- estimate the overall prevalence of childhood stunting;
- compare stunting prevalence across household wealth quintiles;
- examine the distribution of Height-for-Age Z-scores (HAZ) among children under five years of age;
- describe the relationship between household wealth and childhood stunting.



## 4. Dataset

This study used data from the 2018 Nigeria Demographic and Health Survey (NDHS) Kids Recode (KR) dataset. The KR dataset contains information on children born to interviewed women and includes demographic, socioeconomic, maternal, household, health, nutrition, and anthropometric variables.

The original dataset contained 33,924 observations and 1,166 variables. For this study, only variables relevant to the research question were selected and extracted to create a research dataset.



## 5. Study Population

The study population consisted of children under five years of age included in the 2018 Nigeria DHS Kids Recode dataset.

Children with valid Height-for-Age Z-score (HAZ) measurements were included in the analytical dataset. Records with missing or flagged anthropometric measurements were excluded from analyses involving childhood stunting.



## 6. Variables

The following variables were included in the analysis.

| **Variable** | **Description**                      |
|--------------|--------------------------------------|
| hw70         | Height-for-Age Z-score (HAZ)         |
| stunted      | Derived binary outcome (HAZ < -2 SD) |
| v190         | Household wealth index               |
| v106         | Mother's highest educational level   |
| v012         | Mother's age (years)                 |
| b19          | Child's age (months)                 |
| v025         | Place of residence (Urban/Rural)     |



## 7. Methods

A research dataset was created by selecting variables relevant to the study objectives.

Data cleaning included:

- conversion of variables to appropriate data types;
- handling of missing anthropometric measurements;
- exclusion of flagged HAZ observations;
- creation of a binary childhood stunting variable using the WHO definition (HAZ < -2 SD);
- validation of the cleaned dataset using assertions.

Descriptive statistics were generated for continuous variables. Overall childhood stunting prevalence and wealth-specific prevalence were calculated. Results were summarized using tables and graphical visualizations, including a bar chart of stunting prevalence by household wealth quintile and a histogram of Height-for-Age Z-score distribution.

No inferential statistical analyses were performed during this stage of the study.



## 8. Results

A total of 33,924 records were available in the original Nigeria DHS 2018 KR dataset. After restricting the analysis to children with valid Height-for-Age Z-score (HAZ) measurements, 11,364 children were included in the analytical dataset.

The overall prevalence of childhood stunting was 36.16%.

Stunting prevalence differed across household wealth quintiles:

| **Household Wealth** | **Stunting Prevalence (%)** |
|----------------------|-----------------------------|
| Poorest              | 54.98                       |
| Poorer               | 47.05                       |
| Middle               | 36.27                       |
| Richer               | 24.64                       |
| Richest              | 15.73                       |

The distribution of HAZ scores was centred below the WHO reference median, with a mean HAZ of -1.50 SD (SD = 1.58). The histogram showed that most children had HAZ values below zero, indicating generally poorer linear growth compared with the WHO reference population.

The bar chart demonstrated a clear decreasing trend in stunting prevalence as household wealth increased.



## 9. Interpretation

The descriptive analysis indicates a clear inverse association between household wealth and childhood stunting among children under five years of age in Nigeria.

Children from poorer households experienced substantially higher stunting prevalence than children from wealthier households. The progressive decline in stunting prevalence across wealth quintiles suggests that household socioeconomic status is closely associated with child nutritional outcomes.

The overall mean Height-for-Age Z-score was below the WHO reference median, indicating that children in the analytical population generally had poorer linear growth than the international reference population.

Because this study was based on descriptive analyses, the findings demonstrate association rather than causation. Additional inferential analyses would be required to determine statistical significance and evaluate the independent effect of household wealth after adjusting for potential confounding variables.



## 10. Public Health Implications

The findings suggest that childhood stunting remains an important public health challenge among children under five years of age in Nigeria.

The substantially higher prevalence of stunting among children living in poorer households indicates that nutrition interventions should prioritize populations at greatest risk.

Reducing childhood stunting is likely to require coordinated efforts that extend beyond the health sector, including improvements in household socioeconomic conditions, food security, maternal education, water and sanitation, and access to quality healthcare.

Continued monitoring of childhood growth indicators through national surveys and routine health information systems is essential for evaluating progress and informing public health policy.

Future studies should investigate additional determinants of childhood stunting, including maternal education, place of residence, sanitation, and other socioeconomic and environmental factors.



## 11. Limitations

This study has several limitations.

First, the analysis was limited to descriptive statistics and did not include inferential statistical testing.

Second, potential confounding variables were not adjusted for during the analysis.

Third, only selected variables relevant to the study objectives were included in the analytical dataset.

Finally, the cross-sectional nature of the DHS dataset limits the ability to draw causal conclusions regarding the relationship between household wealth and childhood stunting.



## 12. Conclusion

This study found that childhood stunting affected more than one-third of children with valid anthropometric measurements in the analytical dataset.

A clear inverse association was observed between household wealth and childhood stunting, with children from poorer households experiencing substantially higher stunting prevalence than those from wealthier households.

These findings highlight the importance of addressing socioeconomic inequalities as part of comprehensive strategies to reduce childhood stunting in Nigeria.

Further analytical work using inferential statistical methods is recommended to better understand the independent determinants of childhood stunting and to support evidence-based public health decision-making.

