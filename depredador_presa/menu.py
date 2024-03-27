from predator_prey import PredatorPrey
from constants import *
from config import Config
from graphics_plotter import GraphicsPlotter

class Menu():
    '''
    Class to show the menu of the simulation
    '''

    def __init__(self):
        '''
        Constructor of the class
        '''
        self.config = Config()

    def show_options(self):
        '''
        Show the options of the menu
        '''
        while True:
            print(OPTION_1)
            print(OPTION_2)
            option = input(SELECT_OPTION)
            if option == "1":
                print(MENU)
                variable_option = int(input(SELECT_OPTION))
                print(START_SIMULATION)
                self.config.load_variables(variable_option)
                predator_prey = PredatorPrey()
                time_result, preys_result, predators_result = predator_prey.run(
                    dt=self.config.dt,
                    initial_time=self.config.initial_time,
                    initial_preys=self.config.hares,
                    initial_predators=self.config.foxes,
                    preys_birth_rate=self.config.hares_birth_rate,
                    preys_death_rate=self.config.hares_death_rate,
                    predators_birth_rate=self.config.foxes_birth_rate,
                    predators_death_rate=self.config.foxes_death_rate,
                    elapsed_time=self.config.weeks,
                    land_capacity=self.config.land_capacity
                )
                print("Times: ", time_result)
                print("Preys: ", preys_result)
                print("Predators: ", predators_result)
                plotter = GraphicsPlotter()
                plotter.plot_population_variation(time_result, preys_result, predators_result)
                plotter.plot_population_variation_with_both_axes(time_result, preys_result, predators_result)
                plotter.plot_phase_diagram(preys_result, predators_result)
                print(END_SIMULATION)
                break
            elif option == "2":
                print(EXIT)
                break
            else:
                print(INVALID_OPTION)