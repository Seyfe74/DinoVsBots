# CLASS: Dinosaur
# Author: Aferu Minas
# Create Date: August 11, 2021


from weapon import Weapon

class  Dinosaur:
    #Constructor

    def __init__(self,name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
        #self.attacking = False
        
    
        


    # Method

    # def attack(self, name, attacking):
    #     self.name = name
    #     self.attacking = attacking
    #     #self.attack_power = attack_power 
        
    #     print(name + " is attacking Robo1 with fire ball intensity " + str(self.attack_power))