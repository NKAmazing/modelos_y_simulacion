from config import Config
import numpy as np

class PredatorPrey():
    '''
    Class to simulate the predator-prey model
    '''
    
    def __init__(self):
        '''
        Constructor of the class
        '''
        # self.config = Config()
        # self.config.load_variables(1)
        # self.land_capacity = self.config.land_capacity

    def run(self, dt, initial_time, initial_preys, initial_predators, preys_birth_rate, preys_death_rate, 
            predators_birth_rate, predators_death_rate, elapsed_time, land_capacity):
        '''
        Execute the simulation of the predator-prey model
        '''

        preys_list = [initial_preys]
        predators_list = [initial_predators]
        time_list = [initial_time]

        time = initial_time

        for i in range(initial_time, elapsed_time):
            time = time + dt
            hunt_encounter_value = self.hunt_event(preys_list[-1], predators_list[-1])
            actual_capacity = self.get_actual_capacity(preys_list[-1], land_capacity)
            preys_updated = self.get_variations_preys(preys_list[-1], dt, land_capacity, actual_capacity, preys_birth_rate, hunt_encounter_value, preys_death_rate)
            predators_updated = self.get_variations_predators(predators_list[-1], dt, predators_death_rate, hunt_encounter_value, predators_birth_rate)
            preys_list.append(preys_updated)
            predators_list.append(predators_updated)
            time_list.append(time)

        return np.array(time_list), np.array(preys_list), np.array(predators_list)
        

    def hunt_event(self, actual_preys, actual_predators):
        '''
        Calculate the number of preys and predators after the hunt event
        '''
        hunt_encounter_value = actual_preys * actual_predators
        return hunt_encounter_value
    
    def get_variations_preys(self, actual_preys, dt, land_capacity, actual_capacity, preys_birth_rate, hunt_encounter_value, preys_death_rate):
        '''
        Calculate the number of preys
        '''
        if actual_capacity == 0:
            preys_rate = 0
        else:
            preys_rate = (1/land_capacity) * actual_capacity * preys_birth_rate * actual_preys
        preys_variation = actual_preys + dt * (preys_rate - preys_death_rate * hunt_encounter_value)
        return preys_variation
    
    def get_variations_predators(self, actual_predators, dt, predators_death_rate, hunt_encounter_value, predators_birth_rate):
        '''
        Calculate the number of predators
        '''
        predators_survival = actual_predators * predators_death_rate
        predators_variation = actual_predators + dt * ((predators_birth_rate * hunt_encounter_value) - predators_survival)
        return predators_variation
    
    def get_actual_capacity(self, actual_preys, land_capacity):
        '''
        Calculate the actual capacity of the land
        '''
        return land_capacity - actual_preys
