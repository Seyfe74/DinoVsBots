# CLASS: Robot
# Author: Aferu Minas
# Create Date: August 11, 2021


from weapon import Weapon

class  Robot:
    #Constructor

    def __init__(self,name):
        self.name = "  "
        self.health = 10
        self.weapon = " "
        self.attacking = False
        
    
        


    # Method

    def attack(self, name, attacking, weapon):
        self.name = name
        self.attacking = attacking
        self.weapon = weapon
        
        print(name + " is attacking Dino1 with " + weapon)
    




