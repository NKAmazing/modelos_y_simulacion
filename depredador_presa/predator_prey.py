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
        self.config = Config()
        self.config.load_variables()
        self.land_capacity = self.config.land_capacity

    def run(self, dt, initial_time, initial_preys, initial_predators, preys_birth_rate, predators_death_rate, elapsed_time):
        '''
        Execute the simulation of the predator-prey model
        '''

        preys_list = [initial_preys]
        predators_list = [initial_predators]
        time_list = [initial_time]

        time = initial_time

        for i in range(initial_time, 10):
            time = time + dt
            preys_loss_rate_after_hunt, predators_growth_rate_after_hunt, hunt_encounter_value = self.hunt_event(preys_list[-1], predators_list[-1], predators_death_rate)
            actual_capacity = self.get_actual_capacity(preys_list[-1], self.land_capacity)
            preys_updated = self.get_variations_preys(preys_list[-1], preys_loss_rate_after_hunt, dt, self.land_capacity, actual_capacity, preys_birth_rate, hunt_encounter_value)
            predators_updated = self.get_variations_predators(predators_list[-1], dt, predators_death_rate, hunt_encounter_value, predators_growth_rate_after_hunt)
            
            print("Predators updated: ", predators_updated)

            preys_list.append(preys_updated)
            predators_list.append(predators_updated)
            time_list.append(time)

        return np.array(time_list), np.array(preys_list), np.array(predators_list)
        

    def hunt_event(self, actual_preys, actual_predators, predators_death_rate):
        '''
        Calculate the number of preys and predators after the hunt event
        '''
        print("Actual preys del HUNT EVENT: ", actual_preys)
        print("Actual predators del HUNT EVENT: ", actual_predators)
        hunt_encounter_value = actual_preys * actual_predators
        print("Hunt encounter value: ", hunt_encounter_value)
        predators_loss = predators_death_rate * actual_predators
        print("Predators loss del HUNT EVENT: ", predators_loss)
        predators_growth_rate_after_hunt = predators_loss / hunt_encounter_value
        print("Predators growth rate after hunt del HUNT EVENT: ", predators_growth_rate_after_hunt)
        preys_loss_rate_after_hunt = actual_predators / hunt_encounter_value
        return preys_loss_rate_after_hunt, predators_growth_rate_after_hunt, hunt_encounter_value
    
    def get_variations_preys(self, actual_preys, preys_loss_rate_after_hunt, dt, land_capacity, actual_capacity, preys_birth_rate, hunt_encounter_value):
        '''
        Calculate the number of preys
        '''
        if actual_capacity == 0:
            preys_rate = 0
        else:
            preys_rate = (1/land_capacity) * actual_capacity * preys_birth_rate * actual_preys
        preys_variation = actual_preys + dt * (preys_rate + preys_loss_rate_after_hunt * hunt_encounter_value)
        return preys_variation
    
    def get_variations_predators(self, actual_predators, dt, predators_death_rate, hunt_encounter_value, predators_growth_rate_after_hunt):
        '''
        Calculate the number of predators
        '''
        print("Predators: ", actual_predators)
        print("Time variation: ", dt)
        print("Predators death rate: ", predators_death_rate)
        print("Predators growth rate after hunt: ", predators_growth_rate_after_hunt)
        predators_survival = actual_predators * predators_death_rate
        print("Predators survival: ", predators_survival)
        predators_variation = actual_predators + dt * (predators_growth_rate_after_hunt * hunt_encounter_value - predators_survival)
        print("Predators variation: ", predators_variation)
        return predators_variation
    
    def get_actual_capacity(self, actual_preys, land_capacity):
        '''
        Calculate the actual capacity of the land
        '''
        return land_capacity - actual_preys
