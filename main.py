from scenes import scenes
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

play_game()