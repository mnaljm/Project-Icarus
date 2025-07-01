
from time import sleep

# IMPORTS

from scenes import scenes
import os
from time import sleep
from random import randint
#

# FUNCTIONS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_die(sides=20):
    #Rolls a single die with 'sides' number of sides.
    input("Press ENTER to roll the die")
    for i in range(10):
        roll_value = randint(1, sides) # Allows a variable die so we can reuse the same function for different needs.
        # Creates suspense by 'rolling' the number and overwriting the line so it can be used in a scene without disrupting the play.
        print(f'\rRolling... {roll_value:<3}', end='', flush=True)  
        sleep(0.25)           
    die = randint(1, sides)
    print(f'\rYou rolled: {die:<3}') # Again clearing the line so it's clean and doesn't fill the console with rolling.

def play_game():
    clear_screen()
    current_scene = "Opening"
    
    while True:
        clear_screen()
        scene = scenes[current_scene]
        print(scene["text"])
        
        # Show choices:
        print("Available choices:")
        for choice in scene["choices"].keys():
            print(f"- {choice}")
        
        player_choice = input("Enter your choice: ").lower()
        
        if player_choice in scene["choices"]:
            current_scene = scene["choices"][player_choice]
        else:
            print("\033[31mInvalid choice you dumbass, pick one of the choices.\033[0m\n")
            input("press enter to try again")


# BEGIN GAME LOOP
play_game()