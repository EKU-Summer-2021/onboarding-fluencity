'''
   this file contains function probllem and cost
'''
import math

class Problem:
    '''
        this class is for TSP problem
    '''
    def __init__(self, dataset):
        '''
            this function initialize the instance
        '''
        self.dataset = dataset

    def cost(self, index):
        '''
            this function calculate the cost
        '''
        cost_total = 0
        for idx in index:
            if idx == 0:
                continue
            cost_total = cost_total + distance(self.dataset["x"][idx - 1], \
                                               self.dataset["y"][idx - 1], \
                                               self.dataset["x"][idx], self.dataset["y"][idx])
        cost = cost_total + distance \
            (self.dataset["x"][index[0]], \
             self.dataset["y"][index[0]], \
             self.dataset["x"][index[-1]], self.dataset["y"][index[-1]])
        return cost
    def get_dataset(self):
        '''
            this function return dataset
        '''
        return self.dataset

def distance(x_1,y_1, x_2 , y_2 ):
    '''
        this function calculate the distance
    '''
    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
