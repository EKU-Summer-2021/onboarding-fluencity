import unittest

from src import csv_read

from src import TSP_problem,PSO_solver

import numpy as np

class TspTest(unittest.TestCase):

    def test_cost_function(self):
        dataset = csv_read.load_data()
        index = np.array([1,6,7,8,3,4,5,2,9,0])
        problem = TSP_problem(dataset)
        cost = problem.cost(index)
        self.assertEqual(cost,436.5884178216676)

    def test_solve_function(self):
        dataset = csv_read.load_data()
        problem = TSP_problem(dataset)
        psoSolver = PSO_solver(problem)
        path,cost=psoSolver.solve(10, 100)
        self.assertIsInstance(cost,float)
        self.assertIsInstance(path,np.ndarray)