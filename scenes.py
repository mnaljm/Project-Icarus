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
        ),
        "choices": {
            "go_down_stairs": "Opening",
        },
    },
    "TutorialCombat": {
        "text": (
            "You enter a small room where a training dummy stands in the center. "
            "A sign on the wall reads: 'Practice your combat skills here.'\n"
            "You can see a sword and shield lying next to the dummy, ready for you to pick up.\n\n"
        ),
        "choices": {
            "pick_up_sword_and_shield": "CombatTraining",
            "leave_room": "Hallway"
        },
    },
}