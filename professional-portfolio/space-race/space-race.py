# imports
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from iso3166 import countries
from datetime import datetime, timedelta

# notebook presentation
pd.options.display.float_format = '{:,.2f}'.format


'''
PRELIM_EXPLORATION
INPUT: original data frame
OUTPUT: prints shape, column names, total NaN per column
'''
def prelim_exploration(df):
    print('Examining data...')
    shape = df.shape
    print(f'{shape[0]} rows and {shape[1]} columns')
    print(f'Columns: {df.columns}')
    print('Total NaN per column:')
    print(f'{df.isna().sum()}')
    print('Duplicates:')
    print(f'{df.duplicated()}')
      
'''
CLEAN
INPUT: original dataframe
OUTPUT: returns dataframe with duplicates and NaN values removed
'''
def clean(df):
    print('Cleaning data & purging duplicates...')
    # clean NaN values
    cleaned_df = df.dropna()
    # clean duplicates (default keeps 1st, does in place)
    cleaned_df = cleaned_df.drop_duplicates()
    return cleaned_df

'''

'''
def launches_per_org(cleaned_df):
    print('Number of launches per organization: \n')
    data = cleaned_df.Organisation.value_counts()
    print(data)
    bar = px.bar(x=data.index, y=data.values)
    bar.show()
    return

'''
'''
def active_vs_decomissioned(cleaned_df):
    print('Comparison of active vs decomissioned rockets: \n')
    # StatusActive and StatusRetired 
    count = cleaned_df.Rocket_Status.value_counts()
    print(f'{count}\n')
    result = count['StatusActive'] - count['StatusRetired']
    print(f'{result} more Active rockets than Retired rockets')
    return

'''
CHOROPLETH
INPUT
OUTPUT
'''
def choropleth(cleaned_df):
    return

'''
MAIN
run full project suite
'''
def main():
    # read data into data frame
    df = pd.read_csv('mission_launches.csv')
    # perform preliminary data exploration 
    prelim_exploration(df)

    # clean NAN and duplicate data
    cleaned_df = clean(df)

    # descriptive statistics
    print(f' Descriptive statistics for Space Race data:\n {cleaned_df.describe()}')
    # Basic Charts & Grouped Charts
    #launches_per_org(cleaned_df)
    active_vs_decomissioned(cleaned_df)
   
  


    

if __name__ == '__main__':
    main()