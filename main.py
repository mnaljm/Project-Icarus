
from time import sleep

# IMPORTS

from scenes import scenes
import os
from time import sleep
from random import randint
#
player = {
    "hp": 100,
    "damage": 15,
}

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

def match_input(player_choice, choices):
    # Matches user input to available choices, ignoring case and supporting partial matches.
    player_choice = player_choice.lower().strip()

    # First try exact match
    if player_choice in [choice.lower() for choice in choices]:
        return next(choice for choice in choices if choice.lower() == player_choice)
    
    # Goes through the choices and checks if the input is a substring of any choice
    matching_choices = [choice for choice in choices if player_choice in choice.lower()]

    if len(matching_choices) == 1: # If there's only one match, return it
        return matching_choices[0] 
    
    elif len(matching_choices) > 1: # If there are multiple matches, inform the user
        print(f"\033[33mMultiple matches found: {', '.join(matching_choices)}\033[0m")
        print("\033[31mPlease be more specific.\033[0m")
        return None
    
    else:
        print("\033[31mInvalid choice you dumbass, pick one of the choices.\033[0m\n") # If nothing matches mock the user lmao
        return None




def combat_scene(enemy):
    print(f"A wild {enemy['name']} appears! It has {enemy['hp']} HP.\n")
    
    while enemy["hp"] > 0 and player["hp"] > 0:
        action = input("Type 'attack' to fight: ").strip().lower()
        
        if action == "attack":
            enemy["hp"] -= player["damage"]
            print(f"You hit the {enemy['name']} for {player['damage']} damage! (Enemy HP: {max(enemy['hp'], 0)})")
            
            if enemy["hp"] <= 0:
                print(f"You defeated the {enemy['name']}! Combat over.\n")
                input("Press enter to continue...")
                return True
            
            player["hp"] -= enemy["damage"]
            print(f"The {enemy['name']} hits you for {enemy['damage']} damage! (Your HP: {max(player['hp'], 0)})")
            
            if player["hp"] <= 0:
                print("You have been defeated! Game over.")
                return False
        else:
            print("Invalid action. Please type 'attack'.\n")

def play_game():
    clear_screen()
    current_scene = "Opening"
    
    while True:
        clear_screen()
        scene = scenes[current_scene]
        print(scene["text"])

        if scene.get("combat"):
            enemy = scene["enemy"].copy()  # fresh copy for each combat
            combat_result = combat_scene(enemy)
            
            if combat_result is True:
                current_scene = "Hallway"  # example: go back to hallway after combat win
                continue
            elif combat_result is None:
                current_scene = scene["choices"].get("Hallway")
                continue
            else:
                break  # player died or game over

        
        # Show choices:
        print("Available choices:")
        for choice in scene["choices"].keys():
            print(f"- {choice}")
        
        player_choice = input("Enter your choice: ")
        
        matched_choice = match_input(player_choice, scene["choices"].keys())
        
        if matched_choice:
            current_scene = scene["choices"][matched_choice]
        else:

            input("Press Enter to continue...")


# BEGIN GAME LOOP
play_game()