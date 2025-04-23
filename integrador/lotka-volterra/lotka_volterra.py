import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros del modelo
alpha0 = 0.1   # Tasa base de crecimiento de las liebres (con alimentación y sin zorros)
beta = 0.0015   # Tasa de captura de liebres
delta = 0.0003  # Tasa de crecimiento de zorros por liebres capturadas (crecimiento por encuentro)
gamma = 0.2     # Tasa de muerte de zorros (sin liebres)
K = 1500        # Capacidad de carga total del terreno para las liebres
Z = 250         # Capacidad de carga total del terreno para los zorros
A = 0.8         # Amplitud de la variación estacional
T = 365         # Periodo de la variación estacional (un año)

# Sistema de ecuaciones diferenciales
def lotka_volterra(y, t, alpha0, beta, delta, gamma, K, Z, A, T):
    # y = [x, y] donde "x" es la población de liebres e "y" la población de zorros
    x, y = y
    # Variación estacional de la tasa de crecimiento de las liebres
    alpha = alpha0 * (1 + A * np.sin(2 * np.pi * t / T))
    
    # Calcular la sobrepoblación (si la hay)
    hare_overpop = max(0, x - K)
    fox_overpop = max(0, y - Z)
    
    # Ecuación diferencial para la tasa de cambio de las liebres con sobrepoblación (utilizando un factor de 0.01 para reducir la sobrepoblación)
    dxdt = alpha * x * (1 - x / K) - beta * x * y - hare_overpop * 0.01 * x
    # Ecuación diferencial para la tasa de cambio de los zorros con sobrepoblación
    dydt = delta * x * y - gamma * y - fox_overpop * 0.01 * y
    
    return [dxdt, dydt]

# Condiciones iniciales: 500 liebres y 50 zorros
y0 = [40, 9]

# Puntos de tiempo donde se resolverán las ecuaciones
t = np.linspace(0, 500, 10000)

# Resolución de las ecuaciones diferenciales utilizando el método odeint de scipy
sol = odeint(lotka_volterra, y0, t, args=(alpha0, beta, delta, gamma, K, Z, A, T))

# Mostrar los resultados
print("Resultados de la Simulación:")
print("Liebres (x):", sol[:, 0])
print("Zorros (y):", sol[:, 1])

# Graficar los resultados
plt.plot(t, sol[:, 0], label='Liebres (x)')
plt.plot(t, sol[:, 1], label='Zorros (y)')
plt.legend()
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo Presa-Depredador con Capacidad terrenal, Variación Estacional y Sobrepoblación')
plt.show()