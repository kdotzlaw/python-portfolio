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
Input: original data frame
Output: prints shape, column names, total NaN per column
'''
def prelim_exploration(df):
    print('Examining data...')
    shape = df.shape
    print(f'{shape[0]} rows and {shape[1]} columns')
    print(f'Columns: {df.columns}')
    print('Total NaN per column:')
    print(f'{df.isna().sum()}')
      
'''
CLEAN
Input: original dataframe
Output: returns dataframe with duplicates and NaN values removed
'''
def clean(df):
    # clean NaN values
    cleaned_df = df.dropna()
    # clean duplicates

    return cleaned_df

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
   

    

if __name__ == '__main__':
    main()