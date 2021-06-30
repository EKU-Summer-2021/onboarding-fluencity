'''
   this file contains function read csv
'''
import os
import pandas as pd


def load_housing_data(path):
    '''
        this function can load csv file data
    '''
    csv_path = path+"\\10.csv"
    return pd.read_csv(csv_path)
