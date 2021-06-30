from src import csv_read
from src import tsp
import numpy as np

if __name__ == '__main__':
    dataset = csv_read.load_data()
    index=np.arange(len(dataset))
    np.random.shuffle(index)
    cost=tsp.cost(dataset,index)