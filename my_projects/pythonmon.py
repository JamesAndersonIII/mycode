#!/usr/bin/env python3

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
    print("Choose your starting Pythonmon: Bulbasaur, Charmander, or Squirtle.")
    while True:
        starter_pythonmon = input("> ").lower()
        if starter_pythonmon == "1" or starter_pythonmon == "bulbasaur":
            player_pythonmon = "Bulbasaur"
            break
        elif starter_pythonmon == "2" or starter_pythonmon == "charmander":
            player_pythonmon = "Charmander"
            break
        elif starter_pythonmon == "3" or starter_pythonmon == "squirtle":
            player_pythonmon = "Squirtle"
            break
        else:
            print("Please choose Bulbasaur (1), Charmander(2), or Squirtle(3).")

    # Once the player has chosen their starting Pythonmon,
    # We initiate a battle with a wild Pythonmon (Pikachu).
    # We use a while loop to repeatedly prompt the player for their move and the wild Pythonmon's move.
    #TODO Add more skills for Pikachu. (Pretty sure I already have this todo but yeah.)
    #TODO Figure out a way to implement critical attacks for both the user and wild_pythonmon.
    print(f"You have chosen {player_pythonmon} as your starting Pythonmon! Let's begin.")
    print("You have encountered a wild Pythonmon!")
    wild_pythonmon = "Pikachu"
    player_hp = 50
    wild_hp = 50
    wild_attack = 10

    while player_hp > 0 and wild_hp > 0:
        # First, we print out the current HP of both Pythonmon.
        print(f"{player_pythonmon}: {player_hp} HP")
        print(f"{wild_pythonmon}: {wild_hp} HP")

        # Next, we prompt the player to choose their move.
        # They can choose from Tackle or Growl.
        # We use a while loop to ensure the player enters a valid choice.
        #TODO Add skill usage called Power Points or PP per skill. (Tackle (10/10), then after you use it once Tackle (9/10))
        #TODO Add easy to use #'s for the skills like we did to select a starter.
        print("Choose your move: Tackle or Growl.")
        while True:
            player_move = input("> ").lower()
            if player_move == "tackle":
                player_damage = 10
                wild_hp -= player_damage
                print(f"{player_pythonmon} used Tackle!")
                break
            elif player_move == "growl":
                print(f"{player_pythonmon} used Growl! {wild_pythonmon}'s Attack Power had been reduced by -3!")
                wild_attack = max(1, wild_attack - 3)
                break
            else:
                print("Please choose Tackle or Growl.")

        # The wild Pythonmon's move is predetermined in this version of the game.
        # It will always use Thundershock.
        # We print out the move and calculate the damage.
        #TODO Add more skills for Pikachu. (Quick Attack (5/5) wild_pythonmon attacks first always)
        #TODO Add a randomly generated status effect to Thundershock called Paralyzed. (Thundershock has a 15% to Paralyze the starter_pythonmon which, makes the wild_pythonmon attack first.)
        wild_move = "Thundershock"
        print(f"{wild_pythonmon} used {wild_move}!")
        wild_damage = wild_attack
        player_hp -= wild_damage

        # We add a delay of one second to make the game more immersive.
        # This is done using the time module.
        #Cool feature I found during my "too-late" night research.
        import time
        time.sleep(1)

    # Once the battle is over, we print out whether the player won or lost.
    #TODO Add a option to capture Pikachu.
    #TODO Add EXP???!!!! Add Levels????!!!!!!
    if player_hp <= 0:
        print(f"{player_pythonmon} fainted. You have no usable Pythonmon. You black out!")
    else:
        print(f"{wild_pythonmon} fainted. Congratulations, {player_name}! You'll be a Pythonmon Champion in no time!")

if __name__ == "__main__":
    main()


