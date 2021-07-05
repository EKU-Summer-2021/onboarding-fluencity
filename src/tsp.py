'''
Example module for template project.
Pylint will check code in the src directory only!
'''
import math
import numpy as np


class Information:
    '''
        this class store information
    '''
    def __init__(self):
        '''
            this function initialize the instance
        '''
        self.path = []
        self.cost = 500000
    def get_cost(self):
        '''
            this function return cost
        '''
        return self.cost
    def get_path(self):
        '''
            this function return cost
        '''
        return self.path


class TSPSolver:
    '''
        this class is for TSP problem
    '''
    def __init__(self,dataset):
        '''
            this function initialize the instance
        '''
        self.dataset=dataset
        self.best=Information()
    def cost(self,index):
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

    def solve(self,paths,epoches):
        '''
            this function solve the problem
        '''
        path_list=[np.linspace(0,len(self.dataset)-1,\
                len(self.dataset)).astype(int) for
                   _ in range(paths)]
        for index in range(len(path_list)):
            np.random.shuffle(path_list[index])
        velocity_list=[[ np.random.randint(0,len(self.dataset),2),\
                         np.random.randint(0,len(self.dataset),2)] for
                       _ in range(paths)]
        information_list=[Information() for
                          _ in range(paths)]
        for _ in range(epoches):
            for index in range(len(path_list)):
                for velocity in velocity_list[index]:
                    path_list[index]=swap(path_list[index],velocity)
                    if information_list[index].cost>self.cost(path_list[index]):
                        information_list[index].cost=self.cost(path_list[index])
                        information_list[index].path=path_list[index]
                    if self.best.cost>=information_list[index].cost:
                        self.best.cost=information_list[index].cost
                        self.best.path=information_list[index].path
                    break
            for index in range(len(path_list)):
                velocity_list[index][0]=calculate_velocity(path_list[index],self.best.path)
                velocity_list[index][1]=calculate_velocity(path_list[index],\
                                                           information_list[index].path)
        return self.best.path,self.best.cost

def distance(x_1,y_1, x_2 , y_2 ):
    '''
        this function calculate the distance
    '''
    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

def swap(path_list, velocity):
    '''
        this function apply swap
    '''
    temp=path_list[velocity[0]]
    path_list[velocity[0]]=path_list[velocity[1]]
    path_list[velocity[1]]=temp
    return path_list

def calculate_velocity(now,target):
    '''
        this function return velocity
    '''
    order=np.linspace(0, len(target) - 1, len(target)).astype(int)
    np.random.shuffle(order)
    for index_1 in order:
        index_2=0
        for point in now:
            if target[index_1]==point:
                break
            index_2=index_2+1
        if index_2!= 0:
            return np.array([index_1,index_2])
    return np.array([0,0])
