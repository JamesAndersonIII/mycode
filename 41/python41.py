#!/usr/bin/env python3
def main():
    # Define the dictionary of Marvel characters and their stats
 marvelchars = {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    }
}

# Prompt the user for the character and stat they want to know
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ")

# Look up the requested value in the dictionary
value = marvelchars[char_name][char_stat]

# Print the result
print(f"{char_name}'s {char_stat} is: {value}")
main()
