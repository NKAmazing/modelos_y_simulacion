

class Config():
    '''
    Class to load the configuration variables of my simulation
    '''

    def __init__(self):
        pass

    def load_variables(self):
        '''
        Load each variable of the simulation
        '''
        self.hares = 500
        self.foxes = 10
        self.weeks = 600
        self.initial_time = 1
        self.final_time = 600
        self.dt = 1
        self.hares_birth_rate = 0.08
        self.hares_death_rate = 0.002
        self.foxes_birth_rate = 0.0004
        self.foxes_death_rate = 0.2