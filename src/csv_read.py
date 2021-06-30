import pandas as pd
import os

def load_housing_data(path):
    csv_path = os.path.join(path, "10.csv")
    return pd.read_csv(csv_path)

