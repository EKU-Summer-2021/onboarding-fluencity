from src import Problem,Solver,csv_read
import pandas as pd

if __name__ == '__main__':
    dataset = csv_read.load_data()
    problem = Problem(dataset)
    psoSolver=Solver(problem)
    path,cost,solution_list=psoSolver.solve()
    print(f"best cost is {cost} ,best path is {path}")
    psoSolver.solve_restart()
