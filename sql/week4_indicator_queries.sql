-- Week 4: DHS childhood stunting indicators
.headers on
.mode column

-- Q1 - Total records in the cleaned analytical dataset 
SELECT 
    COUNT(*) AS total_records
FROM dhs_stunting;

-- Q2 - Overall stunting prevalence among children with valid HAZ measurements
SELECT 
    COUNT(*) AS valid_children,

    SUM(
        CASE
            WHEN LOWER(stunted) = 'true' THEN 1
            ELSE 0
        END
    ) AS stunted_children,

    ROUND(
        100.0 * 
        SUM(
            CASE
                WHEN LOWER(stunted) = 'true' THEN 1
                ELSE 0
            END
        ) / COUNT(*), 
        2
    ) AS prevalence_percent
FROM dhs_stunting
WHERE LOWER(stunted) IN ('true', 'false');

-- Q3 - Stunting prevalence by household wealth quintile

SELECT
    wealth,

    COUNT(*) AS total_children,

    SUM(
        CASE
            WHEN LOWER(stunted) = 'true' THEN 1
            ELSE 0
        END
    ) AS stunted_children,

    ROUND(
        100.0 * 
        SUM(
            CASE
                WHEN LOWER(stunted) = 'true' THEN 1
                ELSE 0
            END
        ) / COUNT(*), 
        2
    ) AS prevalence_percent

FROM dhs_stunting

WHERE LOWER(stunted) IN ('true', 'false')

GROUP BY wealth

ORDER BY 
    CASE LOWER(wealth)
        WHEN 'poorest' THEN 1
        WHEN 'poorer' THEN 2
        WHEN 'middle' THEN 3
        WHEN 'richer' THEN 4
        WHEN 'richest' THEN 5
        ELSE 6
    END;

--  Q4 - Mean HAZ
SELECT
    ROUND(AVG(haz), 2) AS mean_haz
FROM dhs_stunting
WHERE haz IS NOT NULL;

-- Q5 - Mean child age in the analytical population
SELECT
    ROUND(AVG(child_age), 2) AS mean_child_age
FROM dhs_stunting
WHERE LOWER(stunted) IN ('true', 'false');

--Q6 - Mean maternal age in the analytical population
SELECT
    ROUND(AVG(mother_age), 2) AS mean_mother_age
FROM dhs_stunting
WHERE LOWER(stunted) IN ('true', 'false');
