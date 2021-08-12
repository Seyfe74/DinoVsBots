# CLASS: Battlefield
# Author: Aferu Minas
# Create Date: August 11, 2021

import random

from fleet import Fleet
from herd import Herd

class  Battlefield:
    #Constructor

    def __init__(self,name):
        self.name = name
        

    # Methods

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self ):
        self.dino_attacking = True

    def robo_turn(self):
        self.robo_attacking = True

    def get_rand_numbers (num_1, num_2):
       rand_number = random.randint(num_1, num_2)
       return rand_number   
    damage = get_rand_numbers (2,5)
    print(damage)    

    
    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass


        
    
        


    # Method

    def attack(self, name, attacking, weapon):
        self.name = name
        self.attacking = attacking
        self.weapon = weapon
        
        print(name + " is attacking Dino1 with " + weapon)
    
