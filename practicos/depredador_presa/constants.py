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
                'foxes': 150,
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
                'hares': 500,
                'foxes': 250,
                'weeks': 500,
                'initial_time': 1,
                'final_time': 500,
                'dt': 1,
                'land_capacity': 1500,
                'hares_birth_rate': 0.08,
                'hares_death_rate': 0.002,
                'foxes_birth_rate': 0.0004,
                'foxes_death_rate': 0.2
            },
            3: {
                'hares': 1000,
                'foxes': 5,
                'weeks': 300,
                'initial_time': 1,
                'final_time': 300,
                'dt': 1,
                'land_capacity': 1400,
                'hares_birth_rate': 0.08,
                'hares_death_rate': 0.002,
                'foxes_birth_rate': 0.0004,
                'foxes_death_rate': 0.2
            }
}

RANGE_LIMITS = {
    1: {
        'ax1': 1200,
        'ax2': 90,
    },
    2: {
        'ax1': 1400,
        'ax2': 300,
    },
    3: {
        'ax1': 1200,
        'ax2': 250,
    }
}