#!/usr/bin/python3
import random

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
        'exits': {'north': 'armory', 'east': 'library', 'south': 'entrance', 'west': 'crypt'},
        'items': ['key']
    },
    'armory': {
        'description': 'You have entered an armory. '
                       'The walls are lined with weapons and armor.',
        'exits': {'south': 'hallway'},
        'items': ['sword', 'shield']
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
        'items': ['potion']
    }
    # Add more rooms here maybe...
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

# Define the monsters
monsters = {
    'rat': {
        'description': 'A giant rat appears and attacks you!',
        'health': 20,
        'damage': 5
    },
    'skeleton': {
        'description': 'A rusty skeleton wielding a sword rises from the ground and attacks you!',
        'health': 30,
        'damage': 10
    },
    'troll': {
        'description': 'A large, ugly troll charges at you with its club!',
        'health': 50,
        'damage': 15
    }
}

# Define the puzzles
puzzles = {
    'riddle': {
        'description': 'You come across a door with an inscription that reads:\n'
                       '"I am taken from a mine, and shut up in a wooden case, from which I am never released, '
                       'and yet I am used by almost every human being. What am I?"\n',
        'answer': 'pencil'
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
    'inventory': ['map'],
    'room': random.choice(list(rooms.keys())),
    'moves': 0
}

# Define the game loop
while True:
    # Display the current room and available exits
    room = rooms[player['room']]
    print(room['description'])
    print('Exits:', list(room['exits'].keys()))

    # Display any items in the room
    if 'items' in room:
        for item in room['items']:
            print('You see a', item)

    # Display any monsters in the room
    if 'monster' in room:
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

    # Handle the command
    if not command:
        continue

    verb = command[0]
    noun = ' '.join(command[1:])

    if verb == 'go':
        if noun in room['exits']:
            player['room'] = room['exits'][noun]
            player['moves'] += 1
        else:
            print('You cannot go that way.')
            continue

    elif verb == 'get':
        if 'items' in room and noun in room['items']:
            room['items'].remove(noun)
            player['inventory'].append(noun)
            print(f'You picked up the {noun}.')
        else:
            print(f'There is no {noun} in this room.')
            continue

    elif verb == 'use':
        if noun in player['inventory']:
            # Handle using items
            pass
        else:
            print(f'You do not have a {noun}.')
            continue

    elif verb == 'attack':
        if 'monster' in room:
            # Handle combat
            pass
        else:
            print('There is no monster in this room.')
            continue

    elif verb == 'run':
        if 'monster' in room:
            # Handle escaping combat
            pass
        else:
            print('There is no monster in this room.')
            continue

    elif verb == 'teleport':
        if noun in rooms:
            player['room'] = noun
            player['moves'] += 1
        else:
            print(f'There is no {noun} room.')
            continue

    elif verb == 'help':
        print(
            'Available commands: go [direction], get [item], use [item], attack, run, teleport to [room], help, quit')

    elif verb == 'quit':
        print('Goodbye!')
        break

    else:
        print('Invalid command.')
        continue

    # Handle traps
    if 'trap' in room:
        trap = traps[room['trap']]
        print(trap['description'])
        player['health'] -= trap['damage']
        if player['health'] <= 0:
            print('You died!')
            break

        # Handle puzzles
    if 'puzzle' in room:
        puzzle = puzzles[room['puzzle']]
        if puzzle['answer'].lower() == input('Enter the answer: ').lower():
            print('You solved the puzzle!')
        else:
            print('Incorrect answer.')
            continue

    # Handle winning and losing conditions
    if player['room'] == 'exit':
        print('Congratulations, you escaped the dungeon!')
        print(f'You made it out in {player["moves"]} moves.')
        break

    if player['moves'] >= 50:
        print('You ran out of moves and died of hunger.')
        break

    if player['health'] <= 0:
        print('You died!')
        break
