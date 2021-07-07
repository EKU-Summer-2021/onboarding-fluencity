from src import Problem,Solver,csv_read
import pandas as pd
import numpy as np

if __name__ == '__main__':
    dataset = csv_read.load_data()
    problem = Problem(dataset)
    psoSolver=Solver(problem)
    path,cost,solution_list=psoSolver.solve(10,100)
    save=pd.DataFrame({'cost':[cost],
                 'path':[path]})
    save.to_csv('result.csv', index=False)
    print(f"best cost is {cost} ,best path is {path}")
    print("10 best solution")
    for solution in solution_list[:10]:
        print(f"cost:{solution.cost} and path is {solution.path}")
