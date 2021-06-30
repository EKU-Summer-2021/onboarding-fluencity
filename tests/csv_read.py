import unittest

import pandas

import numpy as np

from src import csv_read


class CsvreadTest(unittest.TestCase):

    def test_return_should_be_dataset(self):
        dataset = csv_read.load_housing_data("..\intelligent_system_data-main\Intelligent System Data\TSP")
        self.assertIsInstance(dataset, pandas.DataFrame)
