# Informative constants used as messages 
OPTION_1 = "1. Iniciar simulación"
OPTION_2 = "2. Salir"
MENU = '''
Seleccione set de variables:
1. Set 1
2. Set 2
3. Set 3
'''
SELECT_OPTION = "Seleccione una opción: "
START_SIMULATION = "Iniciando simulación..."
EXIT = "Saliendo..."
INVALID_OPTION = "Opción no válida"
END_SIMULATION = "Fin de la simulación"
INVALID_VARIABLE_OPTION = "Opción inválida. Cargando configuración por defecto."

# Dictionary with the configuration variables of the simulation
VARIABLE_SETS = {
            1: {
                'hares': 500,
                'foxes': 10,
                'weeks': 500,
                'initial_time': 1,
                'final_time': 500,
                'dt': 1,
                'land_capacity': 1400,
                'hares_birth_rate': 0.08,
                'hares_death_rate': 0.002,
                'foxes_birth_rate': 0.0004,
                'foxes_death_rate': 0.2
            },
            2: {
                'hares': 600,
                'foxes': 20,
                'weeks': 600,
                'initial_time': 1,
                'final_time': 600,
                'dt': 1,
                'land_capacity': 1800,
                'hares_birth_rate': 0.1,
                'hares_death_rate': 0.002,
                'foxes_birth_rate': 0.0008,
                'foxes_death_rate': 0.4
            },
            3: {
                'hares': 700,
                'foxes': 30,
                'weeks': 700,
                'initial_time': 1,
                'final_time': 700,
                'dt': 1,
                'land_capacity': 1500,
                'hares_birth_rate': 0.12,
                'hares_death_rate': 0.002,
                'foxes_birth_rate': 0.0012,
                'foxes_death_rate': 0.6
            }
}