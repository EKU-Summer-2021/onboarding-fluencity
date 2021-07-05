from src import Problem,Solver,csv_read
import numpy as np

if __name__ == '__main__':
    dataset = csv_read.load_data()
    index = np.array([9, 6, 5, 3, 2, 7, 4, 1, 8, 0])
    problem = Problem(dataset)
    psoSolver=Solver(problem)
    path,cost=psoSolver.solve(10,100)
    print(f"cost is {cost} ,path is {type(path)}")
