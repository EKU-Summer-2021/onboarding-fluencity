from src import Problem,Solver,csv_read
import numpy as np

if __name__ == '__main__':
    np.random.seed(1)
    dataset = csv_read.load_data()
    problem = Problem(dataset)
    psoSolver=Solver(problem)
    path,cost=psoSolver.solve(10,100)
    print(f"cost is {cost} ,path is {type(path)}")
