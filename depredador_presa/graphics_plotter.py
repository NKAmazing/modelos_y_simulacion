import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class GraphicsPlotter:
    def __init__(self):
        pass

    def plot_population_variation(self, time_result, preys_result, predators_result):
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

    def plot_phase_diagram(self, preys_result, predators_result):
        plt.close()
        colors = cm.rainbow(np.linspace(0, 1, 2))
        plt.plot(predators_result, preys_result, color=colors[0])
        plt.title("Diagrama de fases")
        plt.xlabel("Zorros")
        plt.xticks(rotation=90)
        plt.ylabel("Liebres")
        plt.show()