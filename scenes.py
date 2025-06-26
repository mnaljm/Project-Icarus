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
#         "THE END - [ENDING NAME]"
#     ),
#     "choices": {}  # Empty choices = game ends
# }

scenes = {
    "Opening": {
    "text": (
        "You wake up in a dark and dingy cell.\n"
        "You see a little light in the wall.\n"
        "you see the light glint off something in the cell.\n\n"
        "Do you want to look at the hole in the wall or the glint.\n"
        "wall or glint\n"
    ),
    "choices": {
        "glint": "cell_glint",
        "wall": "cell_wall"
    },
    "metadata": {  # Optional - for future features
        "location": "cell_block_a",
        "items": ["old_lamp"],
        "npcs": [],
        "visited": False
    }
},
"Stuck": {
    "text": (
        "You have stumbled into a dead end\n\n"
        "THE END - Bad development choice\n"
    ),
    "choices": {}  # Empty choices = game ends
}
}