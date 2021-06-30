import unittest

import pandas

from src import csv_read

from src import tsp

import numpy as np

class TspTest(unittest.TestCase):

    def test_return_should_be_dataset(self):
        dataset = csv_read.load_data()
        index = np.arange(len(dataset))
        np.random.shuffle(index)
        cost = tsp.cost(dataset, index)
        self.assertIsInstance(cost,float)