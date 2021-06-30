import pandas as pd
import os

def load_housing_data(path):
    '''
        this function can load csv file data
    '''
    csv_path = os.path.join(path, "10.csv")
    return pd.read_csv(csv_path)