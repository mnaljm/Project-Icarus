# SCENE DATA TEMPLATE
# This file contains all the scenes for the text adventure game
# Each scene has text content and choices that lead to other scenes

# SCENE STRUCTURE TEMPLATE:
# "scene_name": {
#     "text": (
#         "Your scene description here.\n"
#         "Add atmospheric details and setting information.\n"
#         "Describe what the player sees, hears, and feels.\n\n"
#         "Present the player with clear choices.\n"
#         "(choice1/choice2/choice3)\n"
#     ),
#     "choices": {
#         "choice1": "next_scene_1",
#         "choice2": "next_scene_2",
#         "choice3": "next_scene_3"
#     },
#     "metadata": {  # Optional - for future features
#         "location": "cell_block_a",
#         "items": ["old_key", "rusty_coin"],
#         "npcs": [],
#         "visited": False
#     }
# }

# ENDING SCENE TEMPLATE:
# "ending_scene": {
#     "text": (
#         "Final scene description.\n"
#         "Describe the conclusion of this story path.\n\n"
#         "THE END - [ENDING NAME]
#     ),
#     "choices": {}  # Empty choices = game ends
# }

scenes = {
    "Opening": {
        "text": (
            "You find yourself in a dimly lit room, the air thick with dust and the faint smell of mildew. "
            "The walls are lined with old, peeling wallpaper, and a single flickering light bulb hangs from the ceiling.\n\n"
            "In front of you is a heavy wooden door, slightly ajar, leading to an unknown destination.\n\n"
            "What will you do?\n"
            #"(open_door)"
        ),
        "choices": {
            "open_door": "Hallway",
        },
    },
    "Hallway": {
        "text": (
            "You step into a long, narrow hallway. The walls are lined with faded photographs and the floor creaks under your weight. "
            "At the end of the hallway, you see a staircase leading down into darkness.\n\n"
            "To your left, there is a door slightly ajar, and to your right, another door is closed tightly.\n\n"
            "What will you do?\n"
            #"(go_down_stairs)"
        ),
        "choices": {
            "go_down_stairs": "Opening",

        },
    }
}

def play_game():
    current_scene = "Opening"
    
    while True:
        scene = scenes[current_scene]
        print(scene["text"])
        
        # Show choices:
        print("Available choices:")
        for choice in scene["choices"].keys():
            print(f"- {choice}")
        
        player_choice = input("Enter your choice: ")
        
        if player_choice in scene["choices"]:
            current_scene = scene["choices"][player_choice]
        else:
            print("\033[31mInvalid choice you dumbass, pick one of the choices.\033[0m\n")



play_game()