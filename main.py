from src import csv_read
from src import tsp
import numpy as np

if __name__ == '__main__':
    dataset = csv_read.load_data()
    index=np.array([1,6,7,8,3,4,5,2,9,0])
    cost=tsp.cost(dataset,index)