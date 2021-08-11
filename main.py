from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur

Obj1 = Weapon("W1", 10)
Obj1.fire_weapon("W2", 10)
Obj1.display_weapon()

obj2 = Robot("Robo1")
obj2.attack("Robo2", True, "W4")

obj3 = Dinosaur("Dino1", 5)
obj3.attack("Dino1", True)