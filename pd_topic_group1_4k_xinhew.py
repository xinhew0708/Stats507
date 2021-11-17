# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Filling in Missing Data](#Filling-in-Missing-Data) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide. 

# ## Filling in Missing Data
#
#
# *Xinhe Wang*
#
# xinhew@umich.edu

# ## Fill in Missing Data
#
# - I will introduce some ways of using ```fillna()``` to fill in missing 
# data (```NaN``` values) in a DataFrame.
# - One of the most easiest ways is to drop the rows with missing values.
# - However, data is generally expensive and we do not want to lose all 
# the other columns of the row with missing data.
# - There are many ways to fill in the missing values:
#     - Treat the ```NaN``` value as a feature -> fill in with 0;
#     - Use statistics -> fill in with column mean/median/percentile/a
#     random value;
#     - Use the "neighbors" -> fill in with the last or next values;
#     - Prediction methods -> use regression/machine learning models to 
#     predict the missing value.

# ## Example Data
# - Here we generate a small example dataset with missing values.
#
# - Notice that if we want to indicate if the value in column "b" is larger
# than 0 in column "f", but for the missiing value in column "b", 
# ```df['b'] > 0``` returns ```False``` instead of a ```NaN``` value.
# Therefore, ```NaN``` values need to be delt with before further steps.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 4),
                  columns=['a', 'b', 'c', 'd'])
df.iloc[2, 1] = np.nan
df.iloc[3:5, 0] = np.nan
df['e'] = [0, np.nan, 0, 0, 0]
df['f'] = df['b']  > 0
df

# ## Fill in with a scalar value
# - We can fill in ```NaN``` values with a designated value using 
# ```fillna()```.

df['e'].fillna(0)

df['e'].fillna("missing")

# ## Fill in with statistics (median, mean, ...)
# - One of the most commonly used techniques is to fill in missing values
# with column median or mean.
# - We show an instance of filling in missing values in column "b" with 
# column mean.

df['b'].fillna(df.mean()['b'])

# ## Fill in with forward or backward values
# - We can fill in with the missing values using its "neighber" using 
# ```fillna()```.
# - Can be used if the data is a time series.
# - When the ```method``` argument of ```fillna()``` is set as ```pad``` 
# or ```ffill```, values are filled forward; when ```method``` is set as
# ```bfill```or ```backfill```, values are filled backward.
# - The ```limit``` argument of ```fillna()``` sets the limit of number 
# of rows it is allowed to fill.

df['a'].fillna(method='pad', limit=1)

df['a'].fillna(method='bfill', limit=1)

