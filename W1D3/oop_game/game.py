from game_classes.barbarian import Barbarian
from game_classes.shaman import Shaman
import random

player_1 = Barbarian("Conan") #creating instances
enemy = Shaman("Kyle aka Mystical Mike")


print("Welcome to the game!")
while( player_1.health > 0 and enemy.health > 0):
    response =""
    while not response == "1" and not response == "2":
        print("You are the Barbarian, will you \n 1)Attack \n 2)Heal")
        response = input(">>>") #response will be a string
        if response == "1":
            player_1.attack(enemy)
        elif response == "2":
            player_1.heal()
        else:
            print("please select a valid option")
    enemy_action = random.randint(1,3)
    if enemy_action == 1:
        enemy.attack(player_1)
    if enemy_action == 2:
        enemy.use_totem()
    if enemy_action == 3:
        enemy.heal()

if enemy.health < 0:
    print(f"You have defeated {enemy.name}")
else:
    print(f"The mighty barbarian has fallen")


    
