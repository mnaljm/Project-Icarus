#========================================================================
# IMPORTS
import os
from scenes import scenes # Henter scenes fra scenes.py
#========================================================================

#========================================================================
# FUNCTIONS
def clear_screen():
    #Clears the console
    os.system('cls')


def game():
    # Loop starter
    clear_screen()
    print("Welcome to the Text Adventure Game!")
    print("Type 'exit' to quit at any time.\n")
    current_scene = "Opening"  # Starting scene
    inventory = []  # Player's inventory

    while True:
        scene = scenes.get(current_scene)
        if not scene:
            scene = scenes["Stuck"]  # Fallback to a dead end if scene not found
            input("You have reached a dead end. Press Enter to restart...")
            game()
            

        # Display scene text
        print(scene["text"])

        # Check for exit command
        user_input = input("Choose an option: ").strip().lower()
        if user_input == "exit":
            print("Thanks for playing!")
            break

        # Process choices
        choices = scene["choices"]
        if user_input in choices:
            current_scene = choices[user_input]
        else:
            print("Invalid choice, try again.\n")

#========================================================================

#=========================================================================
# MAIN EXECUTION 
game()
#========================================================================
