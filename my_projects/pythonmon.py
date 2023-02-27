#!/usr/bin/env python3

import time
import random


# Define the starter Pokemon classes.

class Pythonmon:
    def __init__(self, name, max_hp, attack_power, skills):
        self.name = name
        self.max_hp = max_hp
        self.attack_power = attack_power
        self.skills = skills
        self.current_hp = max_hp

    def __str__(self):
        return self.name


class Bulbasaur(Pythonmon):
    def __init__(self):
        super().__init__("Bulbasaur", 45, 10, {
            "Tackle": {
                "power": 10,
                "pp": 10,
                "max_pp": 10
            },
            "Growl": {
                "power": 0,
                "pp": 10,
                "max_pp": 10,
                "effect": "lowers the enemy's attack power by 5"
            }
        })


class Charmander(Pythonmon):
    def __init__(self):
        super().__init__("Charmander", 39, 12, {
            "Scratch": {
                "power": 10,
                "pp": 10,
                "max_pp": 10
            },
            "Growl": {
                "power": 0,
                "pp": 10,
                "max_pp": 10,
                "effect": "lowers the enemy's attack power by 5"
            }
        })


class Squirtle(Pythonmon):
    def __init__(self):
        super().__init__("Squirtle", 44, 9, {
            "Tackle": {
                "power": 10,
                "pp": 10,
                "max_pp": 10
            },
            "Growl": {
                "power": 0,
                "pp": 10,
                "max_pp": 10,
                "effect": "lowers the enemy's attack power by 5"
            }
        })

# Define the wild Pokemon classes


class Pikachu(Pythonmon):
    def __init__(self):
        super().__init__("Pikachu", 35, 8, {
            "Thundershock": {
                "power": 10,
                "pp": 10,
                "max_pp": 10
            }
        })


# Define the PythonBall class

class PythonBall:
    catch_rate = 0.5

# Define the Potion class


class Potion:
    heal_amount = 20


def main():
    # First, we ask the player for their name.
    # This will be used to personalize the game.
    print("Welcome to the world of Pythonmon! What is your name?")
    player_name = input("> ")
    print()

    # Next, we prompt the player to choose their starting Pythonmon.
    # They can choose from Bulbasaur, Charmander, or Squirtle.
    # We use a while loop to ensure the player enters a valid choice.
    print("Choose your starting Pythonmon: Bulbasaur (1), Charmander (2), or Squirtle (3).")
    while True:
        starter_pythonmon = input("> ").lower()
        print()
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

    # Initialize player_hp and wild_hp variables.
    player_hp = player_pythonmon.max_hp
    wild_hp = 0

    # Once the player has chosen their starting Pythonmon,
    # We initiate a battle with a wild Pythonmon (Pikachu).
    # We use a while loop to repeatedly prompt the player for their move and the wild Pythonmon's move.
    print(
        f"You have chosen {player_pythonmon} as your starting Pythonmon! Let's begin.")
    wild_pythonmon = Pikachu()
    player_hp = player_pythonmon.max_hp
    wild_hp = wild_pythonmon.max_hp
    print("You have encountered a wild Pythonmon!")
    print()

    # Added for if the user catches Pikachu.
    game_over = False

    while player_hp > 0 and wild_hp > 0 and not game_over:
        wild_pythonmon = Pikachu()
        player_hp = player_pythonmon.max_hp
        wild_hp = wild_pythonmon.max_hp

        # Prompt the player to choose their move.
        while True:
            if player_hp <= 0:
                print(
                    f"{player_pythonmon.name} fainted. You have no usable Pythonmon. You black out!")
                break
            elif wild_hp <= 0:
                print(
                    f"{wild_pythonmon.name} fainted. Congratulations, {player_name}! You'll be a Pythonmon Champion in no time!")
                break
            print(
                f"{player_pythonmon.name}: {player_hp}/{player_pythonmon.max_hp} HP")
            print(f"{wild_pythonmon.name}: {wild_hp}/{wild_pythonmon.max_hp} HP")
            print(f"What will you do?")
            print("1. Fight")
            print("2. Bag")
            print("3. Pokemon")
            print("4. Run")
            player_choice = input("> ")
            print()
            if player_choice == "1":
                print(f"What move will {player_pythonmon.name} use?")
                for i, skill_name in enumerate(player_pythonmon.skills):
                    skill = player_pythonmon.skills[skill_name]
                    pp = skill["pp"]
                    max_pp = skill["max_pp"]
                    print(f"{i + 1}. {skill_name} ({pp}/{max_pp})")
                while True:
                    skill_index = int(input("> ")) - 1
                    print()
                    if 0 <= skill_index < len(player_pythonmon.skills):
                        skill_name = list(player_pythonmon.skills.keys())[
                            skill_index]
                        skill = player_pythonmon.skills[skill_name]
                        pp = skill["pp"]
                        if pp > 0:
                            skill["pp"] -= 1
                            if skill_name == "Growl":
                                wild_attack_power = max(
                                    wild_pythonmon.attack_power - 5, 1)
                                wild_pythonmon.attack_power = wild_attack_power
                                print(
                                    f"{player_pythonmon.name} used Growl! {wild_pythonmon.name}'s attack power was lowered by 5!")
                                break
                            else:
                                player_damage = skill["power"] + \
                                    player_pythonmon.attack_power
                                wild_hp -= player_damage
                                print(
                                    f"{player_pythonmon.name} used {skill_name}!")
                                print(
                                    f"{wild_pythonmon.name} lost {player_damage} HP.")
                                if wild_hp <= 0:
                                    break
                            pp = skill["pp"]
                            max_pp = skill["max_pp"]
                            print(f"{skill_name} ({pp}/{max_pp})")
                            break
                        else:
                            print("You have no PP left for this move.")
                    else:
                        print("Please choose a valid move.")
                    if wild_hp <= 0:
                        continue
                    break
            elif player_choice == "2":
                print("Which item will you use?")
                print(f"1. PythonBall: {num_pythonballs}")
                print(f"2. Potion: {num_potions}")
                item_choice = input("> ")
                print()
                if item_choice == "1":
                    if num_pythonballs == 0:
                        print("You have no PythonBalls left!")
                    else:
                        num_pythonballs -= 1
                        if random.random() <= PythonBall.catch_rate * (wild_hp / wild_pythonmon.max_hp):
                            if wild_pythonmon.name == "Pikachu":
                                print(
                                    "Congratulations! You caught Pikachu and won the game! You'll be a Pythonmon master in no time!")
                                game_over = True
                                break
                            else:
                                print(f"You caught {wild_pythonmon.name}!")
                                break
                        else:
                            print(f"{wild_pythonmon.name} broke free!")
                        if game_over:
                            break
                elif item_choice == "2":
                    if num_potions == 0:
                        print("You have no Potions left!")
                    else:
                        num_potions -= 1
                        heal_amount = min(Potion.heal_amount,
                                          player_pythonmon.max_hp - player_hp)
                        player_hp += heal_amount
                        print(
                            f"{player_pythonmon.name} was healed for {heal_amount} HP!")
                else:
                    print("Please choose a valid item.")
            elif player_choice == "3":
                print(
                    f"{player_pythonmon.name}: {player_hp}/{player_pythonmon.max_hp} HP")
                print("Skills:")
                for skill_name in player_pythonmon.skills:
                    skill = player_pythonmon.skills[skill_name]
                    print(f"{skill_name} ({skill['pp']}/{skill['pp']})")
                print("")
                continue
            elif player_choice == "4":
                if random.random() <= 0.5:
                    print(
                        "You escaped successfully! I guess you weren't ready to be a Pythonmon Champion.")
                    game_over = True
                    break
                else:
                    print("You could not escape!")
            else:
                print("Please choose a valid option.")

            # The wild Pythonmon's move is predetermined in this version of the game.
            # It will always use Thundershock.
            # We print out the move and calculate the damage.
            if wild_hp > 0:
                wild_skill_name = "Thundershock"
                print(f"{wild_pythonmon.name} used {wild_skill_name}!")
                wild_skill = wild_pythonmon.skills[wild_skill_name]
                wild_damage = wild_skill['power'] + wild_pythonmon.attack_power
                player_hp -= wild_damage
                print(f"{player_pythonmon.name} lost {wild_damage} HP.")
                print()
            else:
                continue

            # Add a delay of one second to make the game more immersive.
            time.sleep(1)


if __name__ == "__main__":
    main()

