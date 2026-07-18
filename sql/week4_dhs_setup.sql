-- Week4: Nigeria DHS Childhood Stunting Study
-- SQLite Database Setup Script
-- This creates a table whose columns match your cleaned research dataset.
DROP TABLE IF EXISTS dhs_stunting;

CREATE TABLE dhs_stunting (
    haz REAL,
    wealth TEXT,
    mother_education TEXT,
    mother_age INTEGER,
    child_age INTEGER,
    residence TEXT,
    stunted INTEGER
);

