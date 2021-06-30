'''
Example module for template project.
Pylint will check code in the src directory only!
'''
import math


def distance(x_1,y_1, x_2 , y_2 ):
    '''
        this function calculate the distance
    '''
    return math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)

def cost(dataset,index):
    '''
        this function calculate the cost
    '''
    cost_total = 0
    for idx in index:
        cost_total = cost_total + distance(dataset["x"][idx], dataset["y"][idx], \
                               dataset["x"][idx], dataset["y"][idx])
    cost = cost_total + distance \
        (dataset["x"][index[0]], \
         dataset["y"][index[0]], dataset["x"][index[-1]], dataset["y"][index[-1]])
    return cost
