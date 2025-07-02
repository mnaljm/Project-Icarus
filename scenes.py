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
#     "metadata": {  
#         "items": ["old_key", "rusty_coin"],
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
            "You wake up in a cold and damp cell, you hear the rats roaming around the floor.\n"
            "The walls are old and slightly crumbling and you hear distant talking through them.\n\n"
            "You manage to get your hands free from the shackles they were placed in.\n\n"
            "What will you do?\n"
        ),
        "choices": {
            "look around cell": "Cell",
            "push through wall": "TutorialCombat",
        },
    },
    # STEALTH
    "Cell": {
        "text": (
            "You look around the cell. The walls are damp and covered in mold, and the air is thick with the smell of decay.\n"
            "A small window high above lets in a sliver of light, revealing a few scattered bones on the floor.\n"
            "In one corner, you see a rusty lockpick lying next to a pile of old rags.\n\n"
            "What will you do?\n"
        ),
        "choices": {
            "lockpick cell door": "Hallway",
        },
        "choice_requirements": {
            "lockpick cell door": {
                "effects": ["unlock"]
            }
        },
        "metadata": {
            "items": ["rusty_lockpick"],
        },
    },
    "Hallway": {
        "text": (
            "You pick the lock on the cell door and it creaks open, revealing a dimly lit hallway.\n"
            "You hear distant footsteps and muffled voices from one end of the corridor.\n"
            "A guard patrols the area, his lantern casting shadows on the cracked stone walls.\n"
            "To your left is a narrow passage with a faint draft — maybe a way out?\n\n"
            "What will you do?\n"
        ),
        "choices": {
            "sneak past the guard": "SneakPastGuard",
            "lure the guard away": "LureGuard",
            "go through narrow passage": "SewerEntrance",
        },
    },
    "SneakPastGuard": {
        "text": (
            "You press yourself against the wall, moving silently with each step as the guard passes by.\n"
            "The lantern flickers and he pauses for a moment, but then continues on.\n"
            "You slip into the shadows and move forward.\n\n"
            "Up ahead, you see a small storeroom with a broken door.\n"
        ),
        "choices": {
            "enter storeroom": "Storeroom",
            "keep moving down the hallway": "SewerEntrance",
        },
        "metadata": {
            "skill_check": {
                "sneak": "easy"
            }
        },
    },
    "LureGuard": {
        "text": (
            "You pick up a loose pebble and toss it toward the far end of the hallway.\n"
            "The sound echoes loudly, and the guard turns, lantern raised.\n"
            "He mutters to himself and walks away to investigate.\n\n"
            "You have a limited time to act.\n"
        ),
        "choices": {
            "sneak into the storeroom": "Storeroom",
            "head through the narrow passage": "SewerEntrance",
        },
    },
    "Storeroom": {
        "text": (
            "Inside the dusty storeroom, you find old tools and supplies.\n"
            "Among the clutter is a small dagger wrapped in cloth and a vial labeled 'sleep draught'.\n"
            "You also spot a torn note: 'Temple lies beyond the roots of fire and ash.'\n\n"
            "What do you take?\n"
        ),
        "choices": {
            "take dagger and vial": "SewerEntrance",
            "just take the note": "SewerEntrance",
            "leave everything": "SewerEntrance",
        },
        "metadata": {
            "items": ["dagger", "sleep_draught", "temple_note"],
            "clue": True,
        },
    },
    "SewerEntrance": {
        "text": (
            "You descend through the narrow passage and find yourself in a foul-smelling tunnel.\n"
            "Slippery stone and the sound of running water greet you.\n"
            "You follow the current until you reach a rusted grate.\n"
            "You hear voices above — guards? Or someone else?\n\n"
            "Do you wait and listen or push through?\n"
        ),
        "choices": {
            "wait and listen": "SewerIntel",
            "push through the grate": "OutsideForest",
        },
    },
    "SewerIntel": {
        "text": (
            "You wait quietly and hear two guards talking above the grate.\n"
            "'The Elder's bandits are moving again. They found something in the woods. A ruin, maybe.'\n"
            "'Yeah, and that crazy priest won't shut up about the gods returning...'\n\n"
            "You note the information before slipping out into the night.\n"
        ),
        "choices": {
            "emerge into the forest": "OutsideForest",
        },
        "metadata": {
            "clue": True,
        },
    },
    "OutsideForest": {
        "text": (
            "You emerge from the sewer into the forest outside the prison. The moon hangs low and mist clings to the trees.\n"
            "Freedom — for now. But the shadows of the Elder's men stretch far.\n"
            "Ahead, you see a faint flickering — a campfire. Could be danger. Could be a lead.\n\n"
            "What will you do?\n"
        ),
        "choices": {
            "approach campfire stealthily": "CampfireScene",
            "avoid camp and head into the woods": "ForestWander",
        },
    },
    # COMBAT
    "TutorialCombat": {
        "text": (
            "You enter a small room where a training dummy stands in the center./n"
            "A sign on the wall reads: 'Practice your combat skills here.\n"
            "You can see a sword lying next to the dummy, ready for you to pick up.\n\n"
            "What will you do?\n"
        ),
        "choices": {
            "prepare for training": "CombatTraining",
        },
        "metadata": {
            "items": ["rusty_sword"],
        },
    },
    "CombatTraining": {
        "text": (
            "You grip the sword and shield firmly. The training dummy stands ready.\n"
            "Prepare to test your skills!\n"
        ),
        "combat": True,
        "enemy": {
            "name": "Training Dummy",
            "hp": 30,
            "damage": 5,
        },
        "alive": True,
        "choices": {
            "leave room": "GuardCorridor",
        },
    },
    "GuardCorridor": {
        "text": (
            "You exit the training room into a broader corridor lined with crumbling statues and torchlight.\n"
            "A guard stands at the far end, talking to another through a grated door.\n"
            "There's no easy way around — you'll need to act.\n\n"
            "What will you do?\n"
        ),
        "choices": {
            "charge the guard": "GuardCombat",
            "intimidate the guard": "IntimidateGuard",
            "look for another way": "BlockedPassage",
        },
    },
    "GuardCombat": {
        "text": (
            "You charge with your sword raised, catching the guard off guard.\n"
            "He fumbles for his weapon as you clash in the corridor.\n"
        ),
        "combat": True,
        "enemy": {
            "name": "Prison Guard",
            "hp": 40,
            "damage": 8,
        },
        "alive": True,
        "choices": {
            "continue forward": "OutsideForest",
        },
    },
    "IntimidateGuard": {
        "text": (
            "You slam your sword into the stone wall, letting sparks fly.\n"
            "'Get out of my way,' you growl.\n"
            "The guard falters, eyes wide, and bolts down the hall.\n\n"
            "You move ahead unchallenged.\n"
        ),
        "choices": {
            "continue forward": "OutsideForest",
        },
        "metadata": {
            "skill_check": {
                "intimidation": "medium",
            }
        }
    },
    "BlockedPassage": {
        "text": (
            "You search the corridor and find a half-collapsed side passage behind a curtain.\n"
            "It looks unstable but just wide enough to squeeze through.\n"
        ),
        "choices": {
            "crawl through passage": "SewerEntrance",
            "go back and fight the guard": "GuardCombat",
        },
    },
}
