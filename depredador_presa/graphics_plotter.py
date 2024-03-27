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
        plt.plot(time_result, preys_result, color=colors[0], label="Liebres")
        plt.plot(time_result, predators_result, color=colors[1], label="Zorros")
        plt.title("Densidad de población de liebres y zorros")
        plt.xlabel("Tiempo (semanas)")
        plt.xticks(rotation=90)
        plt.legend()
        plt.ylabel("Densidad de Población")
        plt.show()

    def plot_population_variation_with_both_axes(self, time_result, preys_result, predators_result):
        '''
        Plot the variation of the population of preys and predators with both axes
        '''
        plt.close()
        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Tiempo (semanas)')
        ax1.set_ylabel('Liebres', color='tab:red')
        ax1.plot(time_result, preys_result, color='tab:red')
        ax1.tick_params(axis='y', labelcolor='tab:red')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Zorros', color='tab:blue')
        ax2.plot(time_result, predators_result, color='tab:blue')
        ax2.tick_params(axis='y', labelcolor='tab:blue')

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