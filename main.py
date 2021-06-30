import numpy as np

from src import Polynomial
from src import csv_read

if __name__ == '__main__':
    coeffs = np.array([1, 0, 0])
    polynom = Polynomial(coeffs)
    dataset = csv_read.load_housing_data("intelligent_system_data-main\Intelligent System Data\TSP")
    print(polynom.evaluate(3))
    print(polynom.roots())
    print(dataset.describe())
