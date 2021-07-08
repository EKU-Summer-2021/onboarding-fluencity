'''
Example module for template project.
Pylint will check code in the src directory only!
'''
from src.polynomial import Polynomial
from src.stored_data import StoredData
from src.problem import Problem
from src.solver import Solver
__all__ = [
    'Polynomial',
    'StoredData',
    'Problem',
    'Solver'
]
