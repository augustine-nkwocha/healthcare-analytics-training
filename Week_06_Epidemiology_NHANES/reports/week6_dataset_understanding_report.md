# Week 6 Dataset Understanding Report

## Project

Association Between Cigarette Smoking and Diabetes Among US Adults Using NHANES 2017–March 2020 Pre-Pandemic Data

## Dataset-Level Summary

| dataset_name   | file_name   |   rows |   columns |   duplicate_rows |   missing_identifier_values |   duplicate_identifier_values |   total_missing_values |   missing_percentage |   memory_usage_bytes |
|:---------------|:------------|-------:|----------:|-----------------:|----------------------------:|------------------------------:|-----------------------:|---------------------:|---------------------:|
| demographics   | P_DEMO.xpt  |  15560 |        29 |                0 |                           0 |                             0 |                  81161 |                17.99 |              3610052 |
| body_measures  | P_BMX.xpt   |  14300 |        22 |                0 |                           0 |                             0 |                 175445 |                55.77 |              2516932 |
| smoking        | P_SMQ.xpt   |  11137 |        16 |                0 |                           0 |                             0 |                 120929 |                67.86 |              1425668 |
| diabetes       | P_DIQ.xpt   |  14986 |        28 |                0 |                           0 |                             0 |                 338049 |                80.56 |              3356996 |

## Demographics

### Variables

| variable_name   | data_type   |   non_missing_values |   missing_values |   missing_percentage |   unique_values |
|:----------------|:------------|---------------------:|-----------------:|---------------------:|----------------:|
| SEQN            | float64     |                15560 |                0 |                 0    |           15560 |
| SDDSRVYR        | float64     |                15560 |                0 |                 0    |               1 |
| RIDSTATR        | float64     |                15560 |                0 |                 0    |               2 |
| RIAGENDR        | float64     |                15560 |                0 |                 0    |               2 |
| RIDAGEYR        | float64     |                15560 |                0 |                 0    |              81 |
| RIDAGEMN        | float64     |                  987 |            14573 |                93.66 |              25 |
| RIDRETH1        | float64     |                15560 |                0 |                 0    |               5 |
| RIDRETH3        | float64     |                15560 |                0 |                 0    |               6 |
| RIDEXMON        | float64     |                14300 |             1260 |                 8.1  |               2 |
| DMDBORN4        | float64     |                15560 |                0 |                 0    |               4 |
| DMDYRUSZ        | float64     |                 3028 |            12532 |                80.54 |               6 |
| DMDEDUC2        | float64     |                 9232 |             6328 |                40.67 |               7 |
| DMDMARTZ        | float64     |                 9232 |             6328 |                40.67 |               5 |
| RIDEXPRG        | float64     |                 1874 |            13686 |                87.96 |               3 |
| SIALANG         | float64     |                15560 |                0 |                 0    |               2 |
| SIAPROXY        | float64     |                15560 |                0 |                 0    |               2 |
| SIAINTRP        | float64     |                15560 |                0 |                 0    |               2 |
| FIALANG         | float64     |                14481 |             1079 |                 6.93 |               2 |
| FIAPROXY        | float64     |                14481 |             1079 |                 6.93 |               2 |
| FIAINTRP        | float64     |                14481 |             1079 |                 6.93 |               2 |
| MIALANG         | float64     |                11000 |             4560 |                29.31 |               2 |
| MIAPROXY        | float64     |                11000 |             4560 |                29.31 |               2 |
| MIAINTRP        | float64     |                11000 |             4560 |                29.31 |               2 |
| AIALANGA        | float64     |                 8224 |             7336 |                47.15 |               3 |
| WTINTPRP        | float64     |                15560 |                0 |                 0    |           13537 |
| WTMECPRP        | float64     |                15560 |                0 |                 0    |           12738 |
| SDMVPSU         | float64     |                15560 |                0 |                 0    |               3 |
| SDMVSTRA        | float64     |                15560 |                0 |                 0    |              24 |
| INDFMPIR        | float64     |                13359 |             2201 |                14.15 |             480 |

### Variables With the Highest Missingness

| variable_name   |   missing_values |   missing_percentage |
|:----------------|-----------------:|---------------------:|
| RIDAGEMN        |            14573 |                93.66 |
| RIDEXPRG        |            13686 |                87.96 |
| DMDYRUSZ        |            12532 |                80.54 |
| AIALANGA        |             7336 |                47.15 |
| DMDEDUC2        |             6328 |                40.67 |
| DMDMARTZ        |             6328 |                40.67 |
| MIAPROXY        |             4560 |                29.31 |
| MIALANG         |             4560 |                29.31 |
| MIAINTRP        |             4560 |                29.31 |
| INDFMPIR        |             2201 |                14.15 |

## Body Measures

### Variables

| variable_name   | data_type   |   non_missing_values |   missing_values |   missing_percentage |   unique_values |
|:----------------|:------------|---------------------:|-----------------:|---------------------:|----------------:|
| SEQN            | float64     |                14300 |                0 |                 0    |           14300 |
| BMDSTATS        | float64     |                14300 |                0 |                 0    |               4 |
| BMXWT           | float64     |                14075 |              225 |                 1.57 |            1513 |
| BMIWT           | float64     |                  588 |            13712 |                95.89 |               3 |
| BMXRECUM        | float64     |                 1470 |            12830 |                89.72 |             512 |
| BMIRECUM        | float64     |                   43 |            14257 |                99.7  |               1 |
| BMXHEAD         | float64     |                  310 |            13990 |                97.83 |             101 |
| BMIHEAD         | float64     |                    0 |            14300 |               100    |               0 |
| BMXHT           | float64     |                13157 |             1143 |                 7.99 |            1110 |
| BMIHT           | float64     |                  171 |            14129 |                98.8  |               2 |
| BMXBMI          | float64     |                13137 |             1163 |                 8.13 |             478 |
| BMDBMIC         | float64     |                 4749 |             9551 |                66.79 |               4 |
| BMXLEG          | float64     |                10984 |             3316 |                23.19 |             260 |
| BMILEG          | float64     |                  488 |            13812 |                96.59 |               1 |
| BMXARML         | float64     |                13490 |              810 |                 5.66 |             366 |
| BMIARML         | float64     |                  487 |            13813 |                96.59 |               1 |
| BMXARMC         | float64     |                13484 |              816 |                 5.71 |             414 |
| BMIARMC         | float64     |                  493 |            13807 |                96.55 |               1 |
| BMXWAIST        | float64     |                12574 |             1726 |                12.07 |            1105 |
| BMIWAIST        | float64     |                  617 |            13683 |                95.69 |               1 |
| BMXHIP          | float64     |                 9862 |             4438 |                31.03 |             834 |
| BMIHIP          | float64     |                  376 |            13924 |                97.37 |               1 |

### Variables With the Highest Missingness

| variable_name   |   missing_values |   missing_percentage |
|:----------------|-----------------:|---------------------:|
| BMIHEAD         |            14300 |               100    |
| BMIRECUM        |            14257 |                99.7  |
| BMIHT           |            14129 |                98.8  |
| BMXHEAD         |            13990 |                97.83 |
| BMIHIP          |            13924 |                97.37 |
| BMIARML         |            13813 |                96.59 |
| BMILEG          |            13812 |                96.59 |
| BMIARMC         |            13807 |                96.55 |
| BMIWT           |            13712 |                95.89 |
| BMIWAIST        |            13683 |                95.69 |

## Smoking

### Variables

| variable_name   | data_type   |   non_missing_values |   missing_values |   missing_percentage |   unique_values |
|:----------------|:------------|---------------------:|-----------------:|---------------------:|----------------:|
| SEQN            | float64     |                11137 |                0 |                 0    |           11137 |
| SMQ020          | float64     |                 9693 |             1444 |                12.97 |               4 |
| SMD030          | float64     |                 3889 |             7248 |                65.08 |              55 |
| SMQ040          | float64     |                 3889 |             7248 |                65.08 |               3 |
| SMQ050Q         | float64     |                 2205 |             8932 |                80.2  |              55 |
| SMQ050U         | float64     |                 2062 |             9075 |                81.49 |               4 |
| SMD057          | float64     |                 2205 |             8932 |                80.2  |              35 |
| SMQ078          | float64     |                 1295 |             9842 |                88.37 |               9 |
| SMD641          | float64     |                 1744 |             9393 |                84.34 |              30 |
| SMD650          | float64     |                 1687 |             9450 |                84.85 |              32 |
| SMD100FL        | float64     |                 1592 |             9545 |                85.71 |               3 |
| SMD100MN        | float64     |                 1592 |             9545 |                85.71 |               3 |
| SMQ670          | float64     |                 1706 |             9431 |                84.68 |               2 |
| SMQ621          | float64     |                 1370 |             9767 |                87.7  |               9 |
| SMD630          | float64     |                   60 |            11077 |                99.46 |              10 |
| SMAQUEX2        | float64     |                11137 |                0 |                 0    |               2 |

### Variables With the Highest Missingness

| variable_name   |   missing_values |   missing_percentage |
|:----------------|-----------------:|---------------------:|
| SMD630          |            11077 |                99.46 |
| SMQ078          |             9842 |                88.37 |
| SMQ621          |             9767 |                87.7  |
| SMD100MN        |             9545 |                85.71 |
| SMD100FL        |             9545 |                85.71 |
| SMD650          |             9450 |                84.85 |
| SMQ670          |             9431 |                84.68 |
| SMD641          |             9393 |                84.34 |
| SMQ050U         |             9075 |                81.49 |
| SMD057          |             8932 |                80.2  |

## Diabetes

### Variables

| variable_name   | data_type   |   non_missing_values |   missing_values |   missing_percentage |   unique_values |
|:----------------|:------------|---------------------:|-----------------:|---------------------:|----------------:|
| SEQN            | float64     |                14986 |                0 |                 0    |           14986 |
| DIQ010          | float64     |                14986 |                0 |                 0    |               4 |
| DID040          | float64     |                 1443 |            13543 |                90.37 |              82 |
| DIQ160          | float64     |                 9516 |             5470 |                36.5  |               3 |
| DIQ180          | float64     |                 9796 |             5190 |                34.63 |               4 |
| DIQ050          | float64     |                 1445 |            13541 |                90.36 |               3 |
| DID060          | float64     |                  427 |            14559 |                97.15 |              46 |
| DIQ060U         | float64     |                  418 |            14568 |                97.21 |               2 |
| DIQ070          | float64     |                 2679 |            12307 |                82.12 |               3 |
| DIQ230          | float64     |                 1443 |            13543 |                90.37 |               6 |
| DIQ240          | float64     |                 1443 |            13543 |                90.37 |               3 |
| DID250          | float64     |                 1107 |            13879 |                92.61 |              20 |
| DID260          | float64     |                 1440 |            13546 |                90.39 |              18 |
| DIQ260U         | float64     |                 1135 |            13851 |                92.43 |               4 |
| DIQ275          | float64     |                 1443 |            13543 |                90.37 |               3 |
| DIQ280          | float64     |                 1218 |            13768 |                91.87 |              75 |
| DIQ291          | float64     |                 1221 |            13765 |                91.85 |               8 |
| DIQ300S         | float64     |                 1433 |            13553 |                90.44 |              99 |
| DIQ300D         | float64     |                 1433 |            13553 |                90.44 |              78 |
| DID310S         | float64     |                 1435 |            13551 |                90.42 |              46 |
| DID310D         | float64     |                 1435 |            13551 |                90.42 |              45 |
| DID320          | float64     |                 1434 |            13552 |                90.43 |             126 |
| DID330          | float64     |                 1349 |            13637 |                91    |              45 |
| DID341          | float64     |                 1430 |            13556 |                90.46 |              26 |
| DID350          | float64     |                 1430 |            13556 |                90.46 |              16 |
| DIQ350U         | float64     |                 1166 |            13820 |                92.22 |               4 |
| DIQ360          | float64     |                 1434 |            13552 |                90.43 |               6 |
| DIQ080          | float64     |                 1434 |            13552 |                90.43 |               3 |

### Variables With the Highest Missingness

| variable_name   |   missing_values |   missing_percentage |
|:----------------|-----------------:|---------------------:|
| DIQ060U         |            14568 |                97.21 |
| DID060          |            14559 |                97.15 |
| DID250          |            13879 |                92.61 |
| DIQ260U         |            13851 |                92.43 |
| DIQ350U         |            13820 |                92.22 |
| DIQ280          |            13768 |                91.87 |
| DIQ291          |            13765 |                91.85 |
| DID330          |            13637 |                91    |
| DID350          |            13556 |                90.46 |
| DID341          |            13556 |                90.46 |
