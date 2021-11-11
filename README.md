# Stats 507, Fall 2021

This is a repository for the course Stats 507: Data Science in Python. 
I will share some course work in this repository as requested in problem set 6.


### Data cleaning script

[data_cleaning.ipynb](data_cleaning.ipynb) reads and cleans the data from the National Health and Nutrition Examination Survey ([NHANES](https://www.cdc.gov/nchs/nhanes/index.htm)). 

The script reads the demographic datasets from 2011 to 2018 and appends them in one data frame, keeping useful columns: id, age, race and ethnicity, education, and marital status, as well as survey weightings. 
It creates a year column to indicate which cohort each case belongs and the resulting data frame is saved in a pickle file ```demographic.pickle```.

It also reads and cleans the oral health and dentation datasets, keeping useful columns: id, dentition exam status, tooth counts, and coronal cavities.
The resulting data frame is saved in a pickle file ```df_oral.pickle```.

This file is written to save cleaned datasets used for subsequent problem sets.

