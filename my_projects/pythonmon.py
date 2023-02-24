#!/usr/bin/env python3

import time
import random

#Define the starter Pokemon classes.

class Bulbasaur:
    name = "Bulbasaur"
    max_hp = 45
    attack_power = 10
    skills = {
        "Tackle": {
            "power": 10,
            "pp": 10
        },
        "Growl": {
            "power": 0,
            "pp": 10
        }
    }

class Charmander:
    name = "Charmander"
    max_hp = 39
    attack_power = 12
    skills = {
        "Scratch": {
            "power": 10,
            "pp": 10
        },
        "Growl": {
            "power": 0,
            "pp": 10
        }
    }

class Squirtle:
    name = "Squirtle"
    max_hp = 44
    attack_power = 9
    skills = {
        "Tackle": {
            "power": 10,
            "pp": 10
        },
        "Tail Whip": {
            "power": 0,
            "pp": 10
        }
    }

# Define the wild Pokemon classes
class Pikachu:
    name = "Pikachu"
    max_hp = 35
    attack_power = 8
    skills = {
        "Thundershock": {
            "power": 10,
            "pp": 10
        }
    }

# Define the PythonBall class
class PythonBall:
    catch_rate = 0.5

# Define the Potion class
class Potion:
    heal_amount = 20


def main():
    # First, we ask the player for their name.
    # This will be used to personalize the game.
    #TODO If time permits add a short backstory.
    #TODO Introduce a Professor (Professor Jimmy ;))
    print("Welcome to the world of Pythonmon! What is your name?")
    player_name = input("> ")

    # Next, we prompt the player to choose their starting Pythonmon.
    # They can choose from Bulbasaur, Charmander, or Squirtle.
    # We use a while loop to ensure the player enters a valid choice.
    #TODO After selection of starter give the user 5 PythonBalls and 10 Potions.
    #TODO Add Potions and functionality. (Potions heal for 20 HP's)
    #TODO Make some functionality for the PythonBalls (Random catch chance, maybe make it easier to catch a Pythonmon if it is low on health)
    #TODO Make a inventory to house PythonBalls and Potions.
    print("Choose your starting Pythonmon: Bulbasaur (1), Charmander (2), or Squirtle (3).")
    while True:
        starter_pythonmon = input("> ").lower()
        if starter_pythonmon == "1" or starter_pythonmon == "bulbasaur":
            player_pythonmon = Bulbasaur()
            break
        elif starter_pythonmon == "2" or starter_pythonmon == "charmander":
            player_pythonmon = Charmander()
            break
        elif starter_pythonmon == "3" or starter_pythonmon == "squirtle":
            player_pythonmon = Squirtle()
            break
        else:
            print("Please choose Bulbasaur (1), Charmander (2), or Squirtle (3).")

    # Give the user 5 PythonBalls and 10 Potions.
    num_pythonballs = 5
    num_potions = 10

    # Once the player has chosen their starting Pythonmon,
    # We initiate a battle with a wild Pythonmon (Pikachu).
    # We use a while loop to repeatedly prompt the player for their move and the wild Pythonmon's move.
    #TODO Add more skills for Pikachu. (Pretty sure I already have this todo but yeah.)
    #TODO Figure out a way to implement critical attacks for both the user and wild_pythonmon.
    print(f"You have chosen {player_pythonmon} as your starting Pythonmon! Let's begin.")
    print("You have encountered a wild Pythonmon!")
   # wild_pythonmon = Pikachu()
   # player_hp = player_pythonmon.max_hp
   # wild_hp = wild_pythonmon.max_hp

    while player_hp > 0 and wild_hp > 0:
        wild_pythonmon = Pikachu()
        player_hp = player_pythonmon.max_hp
        wild_hp = wild_pythonmon.max_hp
        # First, we print out the current HP of both Pythonmon.
        print(f"{player_pythonmon.name}: {player_hp}/{player_pythonmon.max_hp} HP")
        print(f"{wild_pythonmon.name}: {wild_hp}/{wild_pythonmon.max_hp} HP")

        # Prompt the player to choose their move.
    while True:
            print(f"What will you do?")
            print("1. Fight")
            print("2. Bag")
            print("3. Pokemon")
            print("4. Run")
            player_choice = input("> ")
            if player_choice == "1":
                print(f"What move will {player_pythonmon.name} use?")
                for i, skill_name in enumerate(player_pythonmon.skills):
                    skill = player_pythonmon.skills[skill_name]
                    print(f"{i + 1}. {skill_name} ({skill['pp']}/{skill['pp']})")
                while True:
                    skill_index = int(input("> ")) - 1
                    if 0 <= skill_index < len(player_pythonmon.skills):
                        skill_name = list(player_pythonmon.skills.keys())[skill_index]
                        skill = player_pythonmon.skills[skill_name]
                        if skill['pp'] > 0:
                            skill['pp'] -= 1
                            player_damage = skill['power'] + player_python
                            wild_hp -= player_damage
                print(f"{player_pythonmon.name} used {skill_name}!")
                break
            elif player_choice == "2":
                print("Which item will you use?")
                print("1. PythonBall")
                print("2. Potion")
                item_choice = input("> ")
                if item_choice == "1":
                    if num_pythonballs == 0:
                        print("You have no PythonBalls left!")
                        continue
                    num_pythonballs -= 1
                    if random.random() <= PythonBall.catch_rate * (wild_hp / wild_pythonmon.max_hp):
                        print(f"You caught {wild_pythonmon.name}!")
                        break
                    else:
                        print(f"{wild_pythonmon.name} broke free!")
                elif item_choice == "2":
                    if num_potions == 0:
                        print("You have no Potions left!")
                        continue
                    num_potions -= 1
                    player_hp = min(player_hp + Potion.heal_amount, player_pythonmon.max_hp)
                    print(f"{player_pythonmon.name} was healed for {Potion.heal_amount} HP!")
                else:
                    print("Please choose a valid item.")
            elif player_choice == "3":
                print(f"{player_pythonmon.name}: {player_hp}/{player_pythonmon.max_hp} HP")
                print("Skills:")
                for skill_name in player_pythonmon.skills:
                    skill = player_pythonmon.skills[skill_name]
                    print(f"{skill_name} ({skill['pp']}/{skill['pp']})")
            elif player_choice == "4":
                if random.random() <= 0.5:
                    print("You escaped successfully!")
                    break
                else:
                    print("You could not escape!")
            else:
                print("Please choose a valid option.")

        # The wild Pokemon's move is predetermined in this version of the game.
        # It will always use Thundershock.
        # We print out the move and calculate the damage.
wild_skill_name = "Thundershock"
print(f"Pikachu used {wild_skill_name}!")
wild_skill = wild_pythonmon.skills[wild_skill_name]
wild_damage = wild_skill['power'] + wild_pythonmon.attack_power
player_hp -= wild_damage

        # Add a delay of one second to make the game more immersive.
time.sleep(1)

# Once the battle is over, we print out whether the player won or lost.
if player_hp <= 0:
        print(f"{player_pythonmon.name} fainted. You have no usable Pythonmon. You black out!")
else:
        print(f"{wild_pythonmon.name} fainted. Congratulations, {player_name}! You'll be a Pythonmon Champion in no time!")

if __name__ == "__main__":
    main()

