from constants import *

class Config():
    '''
    Class to load the configuration variables of my simulation
    '''

    def __init__(self):
        self.configurations = VARIABLE_SETS

    def load_variables(self, option):
        '''
        Load each variable of the simulation based on the option chosen by the user
        '''
        if option in self.configurations:
            for key, value in self.configurations[option].items():
                setattr(self, key, value)
        else:
            print(INVALID_VARIABLE_OPTION)
            self.load_variables(1)