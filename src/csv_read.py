'''
   this file contains function read csv
'''
import pandas as pd
import urllib.request

def fetch_data():
    '''
        this function can fetch the dataset file
    '''
    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/TSP/10.csv"
    urllib.request.urlretrieve(DOWNLOAD_ROOT, "10.csv")

def load_data():
    '''
        this function can load csv file data
    '''
    fetch_data()
    csv_path = "10.csv"
    return pd.read_csv(csv_path)
