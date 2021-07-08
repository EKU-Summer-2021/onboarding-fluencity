'''
   this file contains function solver
'''
import configparser
import os
import numpy as np
import pandas as pd
from src import StoredData


class Solver:
    '''
        this class is for TSP problem
    '''
    def __init__(self,problem):
        '''
            this function initialize the instance
        '''
        self.best = StoredData()
        self.problem=problem
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../config', 'solver.conf'))
        self.paths = int(config['Parameters']['paths'])
        self.epochs = int(config['Parameters']['epochs'])
        self.restarts=int(config['Parameters']['restarts'])

    def solve(self):
        '''
            this function solve the problem
        '''
        solution_list=[]
        path_list=[np.linspace(0,len(self.problem.dataset)-1,\
                len(self.problem.dataset)).astype(int) for
                   _ in range(self.paths)]
        for index , _ in enumerate(path_list):
            np.random.shuffle(path_list[index])
        velocity_list=[[ np.random.randint(0,len(self.problem.dataset),2),\
                         np.random.randint(0,len(self.problem.dataset),2)] for
                       _ in range(self.paths)]
        information_list=[StoredData() for
                          _ in range(self.paths)]
        for _ in range(self.epochs):
            for index ,_ in enumerate(path_list):
                for velocity in velocity_list[index]:
                    path_list[index]=swap(path_list[index],velocity)
                    solution_list.append(StoredData(path_list[index],\
                                                    self.problem.cost(path_list[index])))
                    if information_list[index].cost>self.problem.cost(path_list[index]):
                        information_list[index].cost=self.problem.cost(path_list[index])
                        information_list[index].path=path_list[index]
                    if self.best.cost>=information_list[index].cost:
                        self.best.cost=information_list[index].cost
                        self.best.path=information_list[index].path
                    break
            for index,_ in enumerate(path_list):
                velocity_list[index][0]=calculate_velocity(path_list[index],self.best.path)
                velocity_list[index][1]=calculate_velocity(path_list[index],\
                                                           information_list[index].path)
        length=len(solution_list)
        for index,_ in enumerate(solution_list):
            for idx in range(index+1,length):
                if solution_list[index].cost>=solution_list[idx].cost:
                    temp=solution_list[index]
                    solution_list[index]=solution_list[idx]
                    solution_list[idx]=temp

        return self.best.path,self.best.cost,solution_list
    def get_problem(self):
        '''
            this function return the problem
        '''
        return self.problem
    def solve_restart(self):
        cost_list=[]
        path_list=[]
        for restart in range(self.restarts):
            path,cost,solution_list=self.solve()
            cost_list.append(cost)
            path_list.append(path)
        save = pd.DataFrame({'cost': cost_list,
                             'path': path_list})
        save.to_csv('result.csv', index=False)
        print(f"the cost {cost_list},the path {path_list}")

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
