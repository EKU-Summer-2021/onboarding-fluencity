'''
Example module for template project.
Pylint will check code in the src directory only!
'''
from src.polynomial import Polynomial
from src.StoredData import StoredData
from src.Problem import Problem
from src.Solver import Solver
__all__ = [
    'Polynomial',
    'StoredData',
    'Problem',
    'Solver'
]
