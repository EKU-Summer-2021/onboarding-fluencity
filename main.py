from src import csv_read
from src import tsp
import numpy as np

if __name__ == '__main__':
    dataset = csv_read.load_data()
    index = np.array([9, 6, 5, 3, 2, 7, 4, 1, 8, 0])
    tspSolver = tsp.TSPSolver(dataset)
    path,cost=tspSolver.solve(10,100)
    print(f"cost is {cost} ,path is {type(path)}")