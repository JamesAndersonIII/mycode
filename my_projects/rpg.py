#!/usr/bin/python3
"""
A text-based adventure game where the player is trapped in a dungeon and must find a way out. The game consists of multiple rooms, each with their own description, items, puzzles, and monsters. The player can move around the dungeon, pick up items, use items, attack monsters, solve puzzles, teleport to different rooms, and view available commands. The game ends when the player either escapes the dungeon, runs out of moves, or dies.

Author and Developer that was WAY OVER THEIR HEAD: James W. Anderson III
"""
import random
import requests

# Cat statue API in entrance.


def get_cat_fact():
    url = "https://cat-fact.herokuapp.com/facts/random"
    response = requests.get(url)
    fact = response.json()["text"]
    return fact


# Print the game instructions
print('Welcome to the darkest dungeon!\n')
print('You are trapped in a dangerous dungeon and must find your way out.')
print('You can move around the dungeon by typing "go" followed by a direction (e.g. "go north").')
print('You can pick up items by typing "get" followed by the item name (e.g. "get sword").')
print('You can use items in your inventory by typing "use" followed by the item name (e.g. "use key").')
print('You can attack monsters in the room by typing "attack".')
print('You can solve puzzles that you find the rooms for some...uhm..."secret items" by typing "puzzle solve". I dont want to know what happens if you are wrong though...')
print('You can run away from monsters by typing "run".')
print('You can teleport to a different room by typing "teleport" followed by the room name (e.g. "teleport library").')
print('You can view the available commands by typing "help".')
print('You can quit the game at any time by typing "quit".\n')

# Define the rooms
rooms = {
    'entrance': {
        'description': 'You are standing in a dimly lit room. '
                       'The walls are damp and the air is thick with dust.',
        'exits': {'north': 'hallway'},
        'items': ['torch']
    },
    'hallway': {
        'description': 'You find yourself in a long, narrow hallway. '
                       'There are several doors on either side of the hallway.',
        'exits': {'north': 'armory', 'east': 'library', 'south': 'locked_door', 'west': 'crypt'},
        'items': ['potion'],
        'monster': None
    },
    'armory': {
        'description': 'You have entered an armory. '
                       'The walls are lined with weapons and armor.',
        'exits': {'south': 'hallway'},
        'items': ['sword', 'shield', 'key'],
        'trap': 'dart'
    },
    'library': {
        'description': 'You are in a vast library. '
                       'Books and scrolls line the walls and fill the shelves.',
        'exits': {'west': 'hallway'},
        'items': ['book', 'scroll']
    },
    'crypt': {
        'description': 'You are in a dark, creepy room. '
                       'Coffins line the walls and skeletons lie scattered about.',
        'exits': {'east': 'hallway'},
        'items': [],
        'puzzle': 'riddle'
    },
    'exit': {
        'description': 'You see a bright light ahead, and hear the sound of rushing water. '
        'You have escaped the dungeon!',
        'exits': {'south': 'locked_door'},
        'items': []
    },
    'locked_door': {
        'description': 'You are in a small room with a locked door. '
        'There is a keyhole on the door.',
        'exits': {'north': 'exit', 'south': 'hallway'},
        'items': []
    }
}

# Define the traps and the damage they do
traps = {
    'dart': {
        'description': 'You stepped on a pressure plate and darts shoot out from the walls!',
        'damage': 10
    },
    'gas': {
        'description': 'You triggered a trap and poisonous gas fills the room!',
        'damage': 20
    },
    'pit': {
        'description': 'You fall into a deep pit and take damage from the fall!',
        'damage': 15
    }
}

# Define the monsters (Not sure I can incorporate this yet :( )
monsters = {
    'rat': {
        'description': 'A giant rat appears and attacks you!',
        'health': 20,
        'damage': 5
    },
    'skeleton': {
        'description': 'A rusty skeleton wielding a sword rises from the ground and attacks you!',
        'health': 30,
        'damage': 7
    },
    'troll': {
        'description': 'A large, ugly troll charges at you with its club!',
        'health': 50,
        'damage': 10
    }
}

# Define the puzzles
puzzles = {
    'riddle': {
        'description': 'You see a riddle written on the wall:\n'
                       '"I am always hungry, I must always be fed. '
                       'The finger I touch, will soon turn red. What am I?"\n',
        'answer': 'fire',
        'reward': 'You hear a clicking sound coming from the wall. '
                  'Upon closer inspection, you discover a hidden compartment containing a key to the exit!'
    },
    'combination': {
        'description': 'You find a safe with a combination lock. '
                       'The lock has 3 dials, each with numbers from 0 to 9.\n',
        'combination': [random.randint(0, 9) for _ in range(3)]
    }
}

# Define the player
player = {
    'health': 100,
    'inventory': ['help', 'cat statue'],
    'room': 'entrance',
    'moves': 0
}

# Define the game loop
while True:
    # Display the current room and available exits
    room = rooms[player['room']]
    print(room['description'])
    print('Exits:', list(room['exits'].keys()))

    # Check if player has reached the exit room
    if player['room'] == 'exit':
        print('Congratulations, you escaped the dungeon!')
        print(f'You made it out in {player["moves"]} moves.')
        break

    # Display any items in the room
    if 'items' in room:
        for item in room['items']:
            print('You see a', item)

    # Display any monsters in the room (Not sure I can incorporate this yet :( )
    if 'monster' in room and room['monster'] is not None:
        monster = monsters[room['monster']]
        print(monster['description'])

    # Display any puzzles in the room
    if 'puzzle' in room:
        puzzle = puzzles[room['puzzle']]
        print(puzzle['description'])

    # Display the player's inventory
    if player['inventory']:
        print('Inventory:', player['inventory'])

    # Prompt the player for a command
    command = input('> ').lower().split()
    print()

    # Handle the command
    if not command:
        continue

    verb = command[0]
    noun = ' '.join(command[1:])

    if verb == 'go':
        if noun in room['exits']:
            # Check if player is trying to enter locked_door room from north (Ran into this issue a few times)
            if noun == 'north' and player['room'] == 'locked_door' and 'key' not in player['inventory']:
                if 'torch' not in player['inventory']:
                    trap = random.choice(list(traps.keys()))
                    print(traps[trap]['description'])
                    player['health'] -= traps[trap]['damage']
                    print(f'Current HP: {player["health"]}')
                    if player['health'] <= 0:
                        print('You died!')
                        break
                else:
                    print('The door is locked. Maybe you should look for a key.')
            else:
                player['room'] = room['exits'][noun]
                player['moves'] += 1
        else:
            print('You cannot go that way.')
            continue

    elif verb == 'use':
        if noun in player['inventory']:
            if player['room'] == 'locked_door' and noun == 'key':
                print('You unlock the door and escape the dungeon!')
                break
            elif noun == 'cat statue':  # corrected indentation
                if 'cat statue' in player['inventory']:
                    print(get_cat_fact())
                else:
                    print('You do not have the cat statue.')
                    continue
            else:
                print(f'You cannot use the {noun} here. Duh...')
                continue
        else:
            print(f'You do not have a {noun}. Maybe go look elsewhere?')
            continue

    elif verb == 'attack':
        if 'monster' in room:
            # Handle combat (hopefully)
            pass
        else:
            print('There is no monster in this room. You are wasting your breath.')
            continue

    elif verb == 'run':
        if 'monster' in room:
            # Handle escaping combat (hopefully)
            pass
        else:
            print('There is nowhere to run (Muahahahahahaa..*cough*).')
            continue

    elif verb == 'teleport':
        if noun in rooms:
            player['room'] = noun
            player['moves'] += 1
        else:
            print(f'There is no {noun} room.')
            print()
            continue

    elif verb == 'help':
        print(
            'Available commands: go [direction], get [item], use [item], attack, puzzle solve, run, teleport [room], help, quit')
        print(f'Current HP: {player["health"]}')
        print()

    elif verb == 'puzzle' and noun == 'solve':
        if 'puzzle' in room and room['puzzle'] in puzzles:
            puzzle = puzzles[room['puzzle']]
            print(puzzle['description'])
            answer = input('Enter your answer: ')
            if answer.lower() == puzzle['answer'].lower():
                print(puzzle['reward'])
                player['inventory'].append('key')
                print('You found a key! This has to be important!')
                print()
            else:
                print('Incorrect answer. You burst out in flames.')
                print('You died!')
                break
        else:
            print('There is no puzzle in this room.')
            continue
    elif verb == 'quit':
        print('Goodbye!')
        break

    else:
        print('Invalid command.')
        continue

    # Handle winning and losing conditions
    if player['room'] == 'exit':
        print('Congratulations, you escaped the dungeon!')
        print(f'You made it out in {player["moves"]} moves.')
        break

    if player['moves'] >= 25:
        print('You ran out of moves and died of hunger.')
        break

    if player['health'] <= 0:
        print('You died!')
        break

