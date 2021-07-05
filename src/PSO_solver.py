'''
   this file contains function solver
'''
import numpy as np
from src import Data

class PSO_solver:
    '''
        this class is for TSP problem
    '''
    def __init__(self,problem):
        '''
            this function initialize the instance
        '''
        self.best = Data()
        self.problem=problem

    def solve(self,paths,epoches):
        '''
            this function solve the problem
        '''
        path_list=[np.linspace(0,len(self.problem.dataset)-1,\
                len(self.problem.dataset)).astype(int) for
                   _ in range(paths)]
        for index in range(len(path_list)):
            np.random.shuffle(path_list[index])
        velocity_list=[[ np.random.randint(0,len(self.problem.dataset),2),\
                         np.random.randint(0,len(self.problem.dataset),2)] for
                       _ in range(paths)]
        information_list=[Data() for
                          _ in range(paths)]
        for _ in range(epoches):
            for index in range(len(path_list)):
                for velocity in velocity_list[index]:
                    path_list[index]=swap(path_list[index],velocity)
                    if information_list[index].cost>self.problem.cost(path_list[index]):
                        information_list[index].cost=self.problem.cost(path_list[index])
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
    def get_problem(self):
        '''
            this function return the problem
        '''
        return self.problem

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
