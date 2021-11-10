# Stats 507, Fall 2021

This is a repository of the course stats 507: Data Science in Python. 
I will share some course work in this repository as requested in problem set 6.


### Data cleaning file

```data_cleaning.ipynb``` ([link](data_cleaning.ipynb)) cleans the data from the National Health and Nutrition Examination Survey ([NHANES](https://www.cdc.gov/nchs/nhanes/index.htm)). 

The script reads the demographic datasets from 2011 to 2018 and appends them in one DataFrame, keeping useful columns: id, age, race and ethnicity, education, and marital status, as well as survey weightings. 
It creates a year column to indicate which cohort each case belongs and the resulting DataFrame is saved in a pickle file ```demographic.pickle```.

It also reads and cleans the oral health and dentation datasets, keeping usingful columns: id, dentition exam status, tooth counts, and coronal cavities.
The resulting DataFrame is saved in a pickle file ```df_oral.pickle```.

This file is written to save cleaned datasets used for subsequent problem sets.

