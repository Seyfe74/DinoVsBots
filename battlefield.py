# CLASS: Battlefield
# Author: Aferu Minas
# Create Date: August 11, 2021


from fleet import Fleet
from herd import Herd

class  Battlefield:
    #Constructor

    def __init__(self,name):
        self.name = "  "
        

    # Methods

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

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
    
