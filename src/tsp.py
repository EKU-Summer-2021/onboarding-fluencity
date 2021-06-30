'''
Example module for template project.
Pylint will check code in the src directory only!
'''
import math


def distance(x1,y1,x2,y2):
    '''
        this function calculate the distance
    '''
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def cost(dataset,index):
    '''
        this function calculate the cost
    '''
    cost = 0
    for idx in index:
        cost = cost + distance(dataset["x"][idx], dataset["y"][idx], dataset["x"][idx], dataset["y"][idx])
    cost = cost + distance \
        (dataset["x"][index[0]], dataset["y"][index[0]], dataset["x"][index[-1]], dataset["y"][index[-1]])
    return cost