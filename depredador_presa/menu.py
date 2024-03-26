from depredador_presa import DepredadorPresa
from constants import *

class Menu():

    def __init__(self):
        pass

    def show_options(self):
        while True:
            print(OPTION_1)
            print(OPTION_2)
            option = input(SELECT_OPTION)
            if option == "1":
                print(START_SIMULATION)
                depredador_presa = DepredadorPresa()
                depredador_presa.run()
            elif option == "2":
                print(EXIT)
                break
            else:
                print(INVALID_OPTION)