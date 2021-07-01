'''
Example module for template project.
Pylint will check code in the src directory only!
'''
import math

class TSPSolver:
    def __init__(self,dataset):
        '''
            this function initialize the instance
        '''
        self.dataset=dataset

    def distance(slef,x_1,y_1, x_2 , y_2 ):
        '''
            this function calculate the distance
        '''
        return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    def cost(self,index):
        '''
            this function calculate the cost
        '''
        cost_total = 0
        for idx in index:
            if idx == 0:
                continue
            cost_total = cost_total + self.distance(self.dataset["x"][idx - 1], self.dataset["y"][idx - 1], \
                                               self.dataset["x"][idx], self.dataset["y"][idx])
        cost = cost_total + self.distance \
            (self.dataset["x"][index[0]], \
             self.dataset["y"][index[0]], self.dataset["x"][index[-1]], self.dataset["y"][index[-1]])
        return cost

    def solve(self):
        '''
            to do
        '''
        return