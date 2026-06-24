-- Week 3B: Basic SQL Queries
-- Dataset: WHO GHO life expectancy indicators

SELECT *
FROM life_expectancy
LIMIT 10;

SELECT DISTINCT Indicator
FROM life_expectancy;

SELECT DISTINCT ParentLocation
FROM life_expectancy;

SELECT DISTINCT Dim1
FROM life_expectancy;

SELECT
    MIN(Period) AS earliest_year,
    MAX(Period) AS latest_year
FROM life_expectancy;


-- Life expectancy at birth only

SELECT *
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
LIMIT 10;

-- Africa only

SELECT *
FROM life_expectancy
WHERE ParentLocation = 
'Africa'
LIMIT 10;

-- Female observations only

SELECT *
FROM life_expectancy
WHERE Dim1 = 
'Female'
LIMIT 10;

-- Year 2021 only

SELECT *
FROM life_expectancy
WHERE Period = 2021
LIMIT 10;

-- Lowest life expectancy at birth in 2021

SELECT
    Location,
    Dim1,
    FactValueNumeric
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
AND Period = 2021
ORDER BY FactValueNumeric ASC
LIMIT 10;

-- Highest life expectancy at birth in 2021

SELECT
    Location,
    Dim1,
    FactValueNumeric
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
AND Period = 2021
ORDER BY FactValueNumeric DESC
LIMIT 10;

-- Average life expectancy by WHO region

SELECT 
ParentLocation,
AVG(FactValueNumeric) AS average_life_expectancy
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
GROUP BY ParentLocation
ORDER BY average_life_expectancy DESC;

--Average life expectancy by sex

SELECT 
Dim1,
AVG(FactValueNumeric) AS average_life_expectancy
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
GROUP BY Dim1
ORDER BY average_life_expectancy DESC;

-- Number of observations by region

SELECT
ParentLocation,
COUNT(*) AS observations
FROM life_expectancy
GROUP BY ParentLocation;

--Earliest and latest life expectancy values by region

SELECT
ParentLocation,
    MIN(FactValueNumeric) AS minimum_life_expectancy,
    MAX(FactValueNumeric) AS maximum_life_expectancy
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
GROUP BY ParentLocation;


--Average life expectancy by region and year

SELECT
    ParentLocation,
    Period,
    AVG(FactValueNumeric) AS average_life_expectancy
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
AND Dim1 =
'Both sexes'
GROUP BY 
    ParentLocation,
    Period
ORDER BY
    ParentLocation,
    Period;

--Summary table

SELECT
    ParentLocation,
    Period,
    AVG(FactValueNumeric) AS average_life_expectancy
FROM life_expectancy
WHERE Indicator = 
'Life expectancy at birth (years)'
AND Dim1 = 'Both sexes'
AND Period IN (2000, 2021)
GROUP BY 
    ParentLocation,
    Period
ORDER BY 
    ParentLocation,
    Period;
