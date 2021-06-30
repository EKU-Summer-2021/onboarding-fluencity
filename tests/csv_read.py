import unittest

import pandas

from src import csv_read


class CsvreadTest(unittest.TestCase):

    def test_return_should_be_dataset(self):
        dataset = csv_read.load_data()
        self.assertIsInstance(dataset, pandas.DataFrame)
