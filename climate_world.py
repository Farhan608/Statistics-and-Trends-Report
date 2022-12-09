# %% [markdown]
# 7PAM2000 Applied Data Science 2
# Assignment 2: Statistics and trends.
# This second assignment will focus on exploring statistics and trends in more detail. You
# are expected to produce a two page report conforming to the guidelines set out below.
# This time you will be exploring public data from the World Bank, and specifically
# country-by-country indicators related to climate change: https://data.worldbank.org/
# topic/climate-change. There are a range of indicators relevant to climate change, for
# example access to electricity, agricultural activity, urban population, etc

# %% [markdown]
# PART A

# %% [markdown]
# Your goal is to:
# • Ingest and manipulate the data using pandas dataframes. Your program should
# include a function which takes a filename as argument, reads a dataframe in Worldbank format and returns two dataframes: one with years as columns and one with
# countries as columns.

# %%
#IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# %% [markdown]
# Function which takes a filename as argument, reads a dataframe in Worldbank format and returns two dataframes: one with years as columns and one with
# countries as columns.

# %%
#FUNCTION THAT TAKES FILENAME AS AN ARGUMENT AND READS DATAFRAME IN THE WORLD-BANK FORMAT 

def read_world_bank_data(filename):
    #read the excel file
    df = pd.read_excel(filename)
    #create a new dataframe with countries as columns
    df_countries = pd.DataFrame(df.iloc[3:,0])
    #create a new dataframe with years as columns
    df_years = pd.DataFrame(df.iloc[3:,1:])
    #rename the columns of the dataframe with countries as columns
    df_countries.columns = ['Country Name']
    #rename the columns of the dataframe with years as columns
    df_years.columns = df.iloc[2,1:]
    #reset the index of the dataframe with countries as columns
    df_countries.reset_index(drop=True, inplace=True)
    #reset the index of the dataframe with years as columns
    df_years.reset_index(drop=True, inplace=True)
    #return the two dataframes
    return df_countries, df_years


# %% [markdown]
# READ THE DATA FROM THE FOLDER NAMED DATA

# %%

#read data colected use the function above to show the data    
df_countries, df_years = read_world_bank_data('API_19_DS2_en_excel_v2_4700532.xls')

# %% [markdown]
# USE THE HEAD FUNCTION TO SEE THE DATA

# %%

df_countries.head()   
df_years.head()

# %% [markdown]
# USE THE HEAD FUNCTION TO SEE THE DATA

# %%
df_years.head()

# %% [markdown]
# PART B

# %% [markdown]
# Explore the statistical properties of a few indicators, that are of interest to you, and
# cross-compare between individual countries and/or the whole world (you do not
# have to do all the countries, just a few will do) and produce appropriate summary
# statistics. You can also use aggregated data for regions and other categories.

# %% [markdown]
# ANAALYZE THE SUMMARY STATISTICS OF THE DATAS

# %%
# produce summary statistics using  as the mean
df_years.mean()

# %%


# %%
# Analyze the summary statistics for each indicator

df_countries.describe()


# %% [markdown]
# USING THE THE GRAPH TO SHOW THE SUMMARY STATISTICS

# %%
#make a graph to show the summary statistics for each indicator
df_years.describe().plot(kind='bar', figsize=(20,20))
plt.title('Summary Statistics for each indicator')
plt.xlabel('Indicators')
plt.ylabel('Values')
plt.show()
    

# %% [markdown]
# PART C

# %% [markdown]
# Explore and understand any correlations (or lack of) between indicators (e.g. population growth and energy consumption). Does this vary between country, have any
# correlations or trends changed with time?

# %% [markdown]
# USE CORRELATION TO ANALYZE THE DATA

# %%
# Analyze the correlation between the indicators
df_years.corr()

# %% [markdown]
# SHOW THE CORELATION BETWEEN THE DATA USING SEA BORN AND MATPLOTLIB LIBRARIES

# %%
#make a graph to show the correlation between the indicators

plt.figure(figsize=(20,20))
sns.heatmap(df_years.corr(), annot=True)
plt.show()

# %% [markdown]
# Again, you are expected to use your initiative and “tell a story” with the data. You
# should use appropriate visualisation 
# 

# %%
#use time series to show the change in the indicators over time
df_years.plot(figsize=(20,20))
plt.title('Change in the indicators over time')
plt.xlabel('Years')
plt.ylabel('Values')
plt.show()
    


