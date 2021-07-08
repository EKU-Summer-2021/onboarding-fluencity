import unittest

from src import csv_read

from src import Problem,Solver

import numpy as np

class TspTest(unittest.TestCase):

    def test_cost_function(self):
        dataset = csv_read.load_data()
        index = np.array([1,6,7,8,3,4,5,2,9,0])
        problem = Problem(dataset)
        cost = problem.cost(index)
        self.assertEqual(cost,467.00165757454954)

    def test_solve_function(self):
        np.random.seed(1)
        dataset = csv_read.load_data()
        problem = Problem(dataset)
        psoSolver = Solver(problem)
        path,cost,solution_list=psoSolver.solve()
        self.assertEqual(cost,324.04770729566593)
        np.allclose(path,np.array([8 ,4 ,5 ,0 ,6 ,1 ,3 ,7 ,2 ,9]))