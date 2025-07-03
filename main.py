# IMPORTS
from scenes import scenes
from items import items
import os
from time import sleep, time
from random import randint
from collections import Counter

import pygame  # Import pygame for audio playback

# Initialize the pygame mixer for audio (do this once at the start)
pygame.mixer.init()

# Load your main menu music file here (make sure the file is in your project folder)
pygame.mixer.music.load("menu_music.mp3")

# PLAYER DATA
player = {
    "hp": 100,
    "damage": 15,
}

player_inventory = []

# SPEEDRUN DATA
speedrun_start_time = None
personal_best = None  # Store only the current session's personal best
player_name = None

# ============================================================================ 
# UTILITY FUNCTIONS
# ============================================================================

def main_menu():
    # Start playing the menu music on loop when main menu loads
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely
    
    while True:  # Add loop to keep returning to menu
        reset_game_state()  # Reset enemies and player each time menu is displayed
        clear_screen()
        reset_all_alive_flags(scenes)

        print("Welcome to Project Icarus!")
        print("1. Start Game")
        print("2. Basic Command List")
        print("3. Start New Run")
        print("4. View Speedrun Leaderboard")
        print("0. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Stop menu music before starting the game
            pygame.mixer.music.stop()
            play_game()
            # After play_game() returns, loop back to menu, music will restart
            pygame.mixer.music.play(-1)
            
        elif choice == "2":
            clear_screen()
            print("Basic Commands:")
            print("- i or inventory: Check your items")
            print("- take [item]: Pick up an item")
            print("- pick up [item]: Pick up an item")
            print("- attack: Engage in combat with an enemy")
            input("\nPress Enter to return to the main menu...")
            # Loop will continue to show menu again
            
        elif choice == "3":
            # Stop menu music before starting a new run
            pygame.mixer.music.stop()
            clear_screen()
            print("Starting a new run...")
            global player_inventory, player_name
            player_inventory = []
            player_name = None  # Reset player name for new run
            play_game()
            # After play_game() returns, loop back to menu, music restarts
            pygame.mixer.music.play(-1)
            
        elif choice == "4":
            show_speedrun_leaderboard()
            
        elif choice == "0":
            print("Thank you for playing! Goodbye!")
            pygame.mixer.music.stop()  # Stop music on exit
            exit(0)
        else:
            print("\033[31mInvalid choice, please try again.\033[0m")
            sleep(1)
            # Loop will continue to show menu again

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
    return die


def reset_all_alive_flags(scenes):
    for scene in scenes.values():
        if "alive" in scene:
            scene["alive"] = True

def skill_check(difficulty):

    # Define difficulty thresholds
    thresholds = {
        "easy": 5,
        "medium": 10, 
        "hard": 15
    }
    
    # Get the required roll for this difficulty
    required_roll = thresholds.get(difficulty.lower(), 10)  # Default to medium if unknown
    
    print(f"\033[33mSkill Check - {difficulty.title()} Difficulty (Need {required_roll}+)\033[0m")
    
    # Roll the die
    roll_result = roll_die(20)
    
    # Check if successful
    success = roll_result >= required_roll
    
    if success:
        print(f"\033[32mSuccess! You rolled {roll_result}, needed {required_roll}+\033[0m")
    else:
        print(f"\033[31mFailure! You rolled {roll_result}, needed {required_roll}+\033[0m")
    
    input("\nPress Enter to continue...")
    return success

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

# ============================================================================
# INVENTORY FUNCTIONS
# ============================================================================

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

# ============================================================================
# COMBAT FUNCTIONS
# ============================================================================

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
                print("\033[31mYou have been defeated.\033[0m \n do you wish to try again? \n yes - no ")

                while True:
                    response = input("Do you wish to try again? (yes - no): ").strip().lower()
                    if response == "yes":
                        main_menu()
                        break
                    elif response == "no":
                        exit()
                    else:
                        print("You must be certain, yes or no.")
                    
                return False
        else:
            print("Invalid action. Please type 'attack'.\n")

# ============================================================================
# REQUIREMENT CHECKING FUNCTIONS
# ============================================================================

def reset_enemies():
    #Resets the 'alive' status of all enemies in all scenes to True.
    for scene_name, scene_data in scenes.items():
        if "combat" in scene_data and scene_data["combat"] is True:
            scene_data["alive"] = True

def reset_player():
    #Reset player stats to default values
    global player
    player["hp"] = 100
    player["damage"] = 15

def reset_game_state():
    #Reset both enemies and player to default state
    reset_enemies()
    reset_player()

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


# ============================================================================
# MINIGAMES
# ============================================================================


def play_dice_poker():
    def roll_dice():
        return [randint(1, 6) for _ in range(5)]

    def evaluate_hand(dice):
        counts = Counter(dice)
        values = list(counts.values())

        if 5 in values:
            return "Five of a kind", 7
        elif 4 in values:
            return "Four of a kind", 6
        elif sorted(values) == [2, 3]:
            return "Full house", 5
        elif 3 in values:
            return "Three of a kind", 4
        elif values.count(2) == 2:
            return "Two pairs", 3
        elif 2 in values:
            return "One pair", 2
        else:
            return "High dice", 1

    def hand_score(dice):
        # Higher total sum helps break ties if needed
        return sum(dice)

    print("Dice Poker Begins!")

    player = roll_dice()
    opponent = roll_dice()

    sleep(1)
    opponent_hand, opponent_rank = evaluate_hand(opponent)
    print(f"Opponent roll: {opponent} → {opponent_hand}")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    player_hand, player_rank = evaluate_hand(player)
    print(f"Your roll: {player} → {player_hand}")

    # Decide the winner
    if player_rank > opponent_rank:
        print("\nYou win! Your hand is stronger.")
    elif player_rank < opponent_rank:
        print("\nYou lose! Opponent's hand is stronger.")
    else:
        # Same rank: use sum of dice to break tie
        player_sum = hand_score(player)
        opponent_sum = hand_score(opponent)
        if player_sum > opponent_sum:
            print("\nYou win! Tie breaker by highest dice sum.")
        elif player_sum < opponent_sum:
            print("\nYou lose! Opponent wins by highest dice sum.")
        else:
            print("\nIt's a draw! Both hands are equally strong.")




def mant_minigame(): #minigame1
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

# ============================================================================
# SKILL CHECK FUNCTIONS
# ============================================================================

def handle_skill_check(choice, scene_name):
    """
    Handle skill checks for a specific choice in a scene.
    
    Args:
        choice (str): The choice that requires a skill check
        scene_name (str): The current scene name
    
    Returns:
        bool: True if skill check passed or no skill check required, False if failed
    """
    scene = scenes[scene_name]
    skill_checks = scene.get("metadata", {}).get("skill_check", {})
    
    if choice in skill_checks:
        difficulty = skill_checks[choice]
        skill_name = choice.replace('_', ' ').title()
        
        print(f"\033[33mAttempting to {skill_name}...\033[0m")
        
        success = skill_check(difficulty)
        
        if not success:
            print(f"\033[31mYou failed to {skill_name.lower()}!\033[0m")
            print("\033[33mYou don't feel confident enough to try that again.\033[0m")
            del scene["choices"][choice]  # Remove the choice from the scene
            input("\nPress Enter to continue...")
            return False
        else:
            print(f"\033[32mYou successfully {skill_name.lower()}!\033[0m")
            return True
    
    return True  # No skill check required, proceed normally

# ============================================================================
# SPEEDRUN FUNCTIONS
# ============================================================================

def start_speedrun_timer():
    """Start the speedrun timer"""
    global speedrun_start_time
    speedrun_start_time = time()

def get_speedrun_time():
    """Get the current speedrun time in seconds"""
    if speedrun_start_time is None:
        return 0
    return time() - speedrun_start_time

def format_time(seconds):
    """Format time in MM:SS.ss format"""
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:05.2f}"

def save_speedrun_time(completion_time):
    """Save a speedrun time and return if it's a personal best"""
    global personal_best
    
    # Check if this is a personal best
    is_personal_best = personal_best is None or completion_time < personal_best
    
    if is_personal_best:
        personal_best = completion_time
    
    return is_personal_best

def show_speedrun_leaderboard():
    """Display the current session's personal best"""
    clear_screen()
    print("=" * 50)
    print("CURRENT SESSION PERSONAL BEST")
    print("=" * 50)
    
    if personal_best is None:
        print("No completed runs in this session yet!")
    else:
        formatted_time = format_time(personal_best)
        current_player = player_name if player_name else "You"
        print(f"Best Time: {formatted_time}")
        print(f"Player: {current_player}")
    
    input("\nPress Enter to return to main menu...")



def get_player_name():
    """Get the player's name for speedrun tracking"""
    global player_name
    if player_name is None:
        clear_screen()
        print("Welcome to Project Icarus Speedrun!")
        print("Please enter your name for the leaderboard:")
        player_name = input("Name: ").strip()
        if not player_name:
            player_name = "Anonymous"
        print(f"Good luck, {player_name}!")
        input("Press Enter to continue...")
    return player_name

# ============================================================================
# MAIN GAME LOOP
# ============================================================================

def play_game():
    clear_screen()
    current_scene = "Opening"
    last_scene = None 
    
    # Get player name at the start for speedrun tracking
    get_player_name()
    
    # Start speedrun timer
    start_speedrun_timer()
    
    while True:
        clear_screen()
        scene = scenes[current_scene]
        print(scene["text"])

        # Check if this is an ending scene (no choices available)
        if not scene["choices"]:
            # Calculate speedrun time
            completion_time = get_speedrun_time()
            formatted_time = format_time(completion_time)
            
            print("\n" + "="*50)
            print("GAME OVER")
            print("="*50)
            print(f"Completion Time: {formatted_time}")
            
            # Save the speedrun time and check for personal best
            is_personal_best = save_speedrun_time(completion_time)
            
            # Display appropriate record message
            if is_personal_best:
                print("🎉 NEW PERSONAL BEST! 🎉")
            
            input("\nPress Enter to return to main menu...")
            return  # Return to main menu

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

        if scene.get("minigame") and scene.get("alive", True):
            if scene.get("alive") == True:
                minigame_type = scene.get("minigame_type")
                if minigame_type == "rps":
                    mant_minigame()  #play rock paper scissor
                elif minigame_type == "dice_poker":
                    play_dice_poker() #play dice poker
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
        
        # Show current speedrun time
        current_time = get_speedrun_time()
        formatted_current_time = format_time(current_time)
        print(f"\nTime: {formatted_current_time}")
        
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
            
            # Handle skill check for the choice
            if not handle_skill_check(matched_choice, current_scene):
                continue  # Stay in current scene if skill check failed
            
            current_scene = scene["choices"][matched_choice]
        else:
            input("Press Enter to continue...")

# ============================================================================
# GAME START
# ============================================================================

# BEGIN GAME LOOP
main_menu()