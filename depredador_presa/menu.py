from predator_prey import PredatorPrey
from constants import *
from config import Config
from graphics_plotter import GraphicsPlotter

class Menu():
    def __init__(self):
        self.config = Config()

    def show_options(self):
        while True:
            print(OPTION_1)
            print(OPTION_2)
            option = input(SELECT_OPTION)
            if option == "1":
                print(START_SIMULATION)
                self.config.load_variables()
                predator_prey = PredatorPrey()
                # Pasamos las variables de configuración al método run()
                time_result, preys_result, predators_result = predator_prey.run(
                    dt=self.config.dt,
                    initial_time=self.config.initial_time,
                    initial_preys=self.config.hares,
                    initial_predators=self.config.foxes,
                    preys_birth_rate=self.config.hares_birth_rate,
                    predators_death_rate=self.config.foxes_death_rate,
                    elapsed_time=self.config.weeks
                )
                print("Times: ", time_result)
                print("Preys: ", preys_result)
                print("Predators: ", predators_result)
                plotter = GraphicsPlotter()
                plotter.plot_population_variation(time_result, preys_result, predators_result)
                plotter.plot_phase_diagram(preys_result, predators_result)
                print(END_SIMULATION)
                break
            elif option == "2":
                print(EXIT)
                break
            else:
                print(INVALID_OPTION)