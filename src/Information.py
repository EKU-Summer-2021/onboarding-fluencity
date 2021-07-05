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

def max(a):
    return a