from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield



robo1 = Robot("Robo1", 10, "W1")
robo2 = Robot("Robo2", 10, "W2")
robo3 = Robot("Robo3", 10, "W3")

dino1 = Dinosaur("Dino1", 10, "Claws")
dino2 = Dinosaur("Dino2", 10, "Bite")
dino3 = Dinosaur("Dino3", 10, "Whips")


f = Fleet()
f = []
f.append(Robot("Robo1  ", 10, "  W1"))
f.append(Robot("Robo2  ", 10, "  W2"))
f.append(Robot("Robo3  ", 10, "  W3"))


h = Herd()
h = []
h.append(Dinosaur("Dino1  ", 10, "  Claws"))
h.append(Dinosaur("Dino2  ", 10, "  Bite"))
h.append(Dinosaur("Dino3  ", 10, "  Whips"))


b = Battlefield("B1")
b.get_rand_numbers



# for obj in f :
#     print(obj.name, obj.health, obj.weapon, sep="")

# for obj in h :
#     print(obj.name, obj.health, obj.attack_power, sep="")    




