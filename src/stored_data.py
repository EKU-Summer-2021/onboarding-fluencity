'''
   this file contains information
'''


class StoredData:
    '''
        this class store information
    '''

    def __init__(self, path=None, cost=500000):
        '''
            this function initialize the instance
        '''
        if path is None:
            path = []
        self.path = path
        self.cost = cost

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
