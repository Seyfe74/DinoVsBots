# CLASS: Weapon
# Author: Aferu Minas
# Create Date: August 11, 2021

class Weapon:
    # Constructor

    def __init__(self, name, attack_power):   
       self.name = "W1"
       self.attack_power = 10
       

    def fire_weapon (self,name, attack_power):
        self.name = name
        self.attack_power = attack_power - 1


    def display_weapon (self):
        print(self.name + "  Has remaining attack power of " + str(self.attack_power) )