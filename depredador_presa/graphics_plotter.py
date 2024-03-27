import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class GraphicsPlotter:
    '''
    Class to plot the results of the predator-prey model
    '''

    def plot_population_variation(self, time_result, preys_result, predators_result):
        '''
        Plot the variation of the population of preys and predators
        '''
        plt.close()
        colors = cm.rainbow(np.linspace(0, 1, 2))
        plt.plot(time_result, preys_result, color='b', label="Liebres")
        plt.plot(time_result, predators_result, color='r', label="Zorros")
        plt.title("Densidad de población de liebres y zorros")
        plt.xlabel("Tiempo (semanas)")
        plt.xticks(rotation=90)
        plt.legend()
        plt.ylabel("Densidad de Población")
        plt.show()

    def plot_population_variation_with_both_axes(self, time_result, preys_result, predators_result, ax1_limit, ax2_limit):
        '''
        Plot the variation of the population of preys and predators with both axes
        '''
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.set_ylim(0, ax1_limit)
        ax2.set_ylim(0, ax2_limit)
        ax1.plot(time_result, preys_result, label="Liebres", color='b')
        ax2.plot(time_result, predators_result, label="Zorros", color='r')
        ax1.set_xlabel("Tiempo (semanas)")
        ax1.set_ylabel("Población de Liebres", color='b')
        ax2.set_ylabel("Población de Zorros", color='r')
        ax1.legend(loc="upper center")
        ax2.legend(loc="upper right")
        fig.tight_layout()
        plt.title("Densidad de población de liebres y zorros")
        plt.show()

    def plot_phase_diagram(self, preys_result, predators_result):
        '''
        Plot the phase diagram of the predator-prey model
        '''
        plt.close()
        colors = cm.rainbow(np.linspace(0, 1, 2))
        plt.plot(predators_result, preys_result, color=colors[0])
        plt.title("Diagrama de fases")
        plt.xlabel("Zorros")
        plt.xticks(rotation=90)
        plt.ylabel("Liebres")
        plt.show()