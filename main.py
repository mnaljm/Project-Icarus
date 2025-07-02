# IMPORTS

from scenes import scenes
from items import items
import os
from time import sleep
from random import randint

# PLAYER DATA
player = {
    "hp": 100,
    "damage": 15,
}

player_inventory=[]

# FUNCTIONS


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_item_to_inventory(item_name):
    #Add an item to player's inventory
    if item_name in items:
        player_inventory.append(item_name)
        item_desc = items[item_name]["description"]
        print(f"\033[32mYou picked up: {item_name.replace('_', ' ').title()}\033[0m")
        print(f"\033[36m{item_desc}\033[0m")
        return True
    return False

def show_inventory():
    #Display player's current inventory
    if not player_inventory:
        print("\033[33mYour inventory is empty.\033[0m")
    else:
        print("\033[36mInventory:\033[0m")
        for item in player_inventory:
            item_name = item.replace('_', ' ').title()
            print(f"- {item_name}")

def handle_special_actions(choice, scene_name):
    #Handle special actions like picking up items
    # Detect item pickup based on choice name
    if choice.startswith("pick up "):
        item_name = choice.replace("pick up ", "")
    elif choice.startswith("take "):
        item_name = choice.replace("take ", "")
    else:
        return False
    
    # Check if the item is available in the current scene's metadata
    scene = scenes[scene_name]
    scene_items = scene.get("metadata", {}).get("items", [])
    
    if item_name in scene_items:
        if add_item_to_inventory(item_name):
            # Remove item from scene metadata so it can't be picked up again
            scene_items.remove(item_name)
            input("\nPress Enter to continue...")
            return False  # Successfully picked up, stay in scene
    else:
        print(f"\033[31mThere is no {item_name.replace('_', ' ')} here to pick up.\033[0m")
        input("\nPress Enter to continue...")
        return True  # Stay in current scene
    return False

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
    hit_chance = 0
    print(f"A wild {enemy['name']} appears! It has {enemy['hp']} HP.\n")
    
    while enemy["hp"] > 0 and player["hp"] > 0:
        action = input("Type 'attack' to fight: ").strip().lower()
        
        if action == "attack":
            total_damage = get_player_total_damage()
            hit_chance = randint (2, 20)
            if enemy["dodge"] < hit_chance:
                enemy["hp"] -= total_damage
                print(f"You hit the {enemy['name']} for {total_damage} damage! (Enemy HP: {max(enemy['hp'], 0)})")
            else:
                print("you missed")
            
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

def get_player_total_damage():
    #Calculate total damage including base damage and weapon bonuses
    total_damage = player["damage"]  # Start with base damage
    
    # Add damage from all weapons in inventory
    for item_name in player_inventory:
        if item_name in items:
            item = items[item_name]
            if item.get("metadata", {}).get("type") == "weapon":
                weapon_damage = item.get("metadata", {}).get("base_stats", {}).get("damage", 0)
                total_damage += weapon_damage
    
    return total_damage

def check_choice_requirements(choice, scene_name):
    #Check if player meets requirements for a choice
    scene = scenes[scene_name]
    choice_requirements = scene.get("choice_requirements", {})
    
    if choice in choice_requirements:
        required_effects = choice_requirements[choice].get("effects", [])
        
        # Check if player has items with required effects
        for effect in required_effects:
            has_effect = False
            for item_name in player_inventory:
                if item_name in items:
                    item_effects = items[item_name].get("metadata", {}).get("effects", [])
                    if effect in item_effects:
                        has_effect = True
                        break
            
            if not has_effect:
                effect_name = effect.replace('_', ' ').title()
                print(f"\033[31mYou need something with {effect_name} ability to do that.\033[0m")
                input("\nPress Enter to continue...")
                return False
    return True

def mant_minigame():
    npcpick = ""
    pick = ""
    score = 0
    npcscore = 0

    while score < 3 and npcscore < 3:
        print("Choose your weapon - (rock, paper, scissor):")
        pick = input("").lower()

        # Random number between 1 and 9
        npcvalue = randint (1, 9)
        if npcvalue <= 3:
            npcpick = "rock"
        elif npcvalue <= 6:
            npcpick = "paper"
        else:
            npcpick = "scissor"

        print(f"NPC chose {npcpick}")

        if pick == npcpick:
            print("It's a draw!")

        elif (pick == "rock" and npcpick == "paper") or \
            (pick == "paper" and npcpick == "scissor") or \
            (pick == "scissor" and npcpick == "rock"):
            npcscore += 1
            print("You lose this round!")

        elif (pick == "rock" and npcpick == "scissor") or \
            (pick == "paper" and npcpick == "rock") or \
            (pick == "scissor" and npcpick == "paper"):
            score += 1
            print("You win this round!")

        else:
            print("Invalid choice, please pick rock, paper, or scissor.")
            continue  # Skip score printing and next loop iteration if invalid input

        print(f"Score - You: {score}, NPC: {npcscore}\n")

    if score == 3:
        print("You won the game!")
    else:
        print("You lost the game!")



def play_game():
    clear_screen()
    current_scene = "Opening"
    last_scene = None 
    
    while True:
        clear_screen()
        scene = scenes[current_scene]
        print(scene["text"])

        

        if scene.get("combat") and scene.get("alive", True):
            if scene.get ("alive") == True:
                enemy = scene["enemy"].copy()
                combat_result = combat_scene(enemy)

                if combat_result is True:
                    scene["alive"] = False
                    last_scene = current_scene
                  # last_scene = None
                    continue
                else:
                    break 


                    pass

            
        
        # Show choices:
        print("Available choices:")
        for choice in scene["choices"].keys():
            print(f"- {choice}")

        # Show items available in the room
        scene_items = scene.get("metadata", {}).get("items", [])
        if scene_items:
            print("\nItems you can see:")
            for item in scene_items:
                item_display = item.replace('_', ' ').title()
                print(f"- {item_display} (use 'take {item}' to pick up)")

        #Print the player inventory option
        print("\nOther commands:")
        print("- inventory (check your items)")
        
        player_choice = input("Enter your choice: ")
        
        if player_choice.lower().strip() in ["inventory", "i"]:
            show_inventory()
            input("Press Enter to continue")
            continue

        # Check for item pickup commands (take/pick up)
        if player_choice.lower().strip().startswith(("take ", "pick up ")):
            if handle_special_actions(player_choice.lower().strip(), current_scene):
                continue  # Stay in current scene after special action
            continue  # Also continue if item was successfully picked up

        matched_choice = match_input(player_choice, scene["choices"].keys())
        
        if matched_choice:
            # Check if player meets requirements for this choice
            if not check_choice_requirements(matched_choice, current_scene):
                continue  # Stay in current scene if requirements not met
                
            # Handle special actions before moving to next scene
            if handle_special_actions(matched_choice, current_scene):
                continue  # Stay in current scene after special action
            
            current_scene = scene["choices"][matched_choice]
        else:

            input("Press Enter to continue...")

# BEGIN GAME LOOP
play_game()