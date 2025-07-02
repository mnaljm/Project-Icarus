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
        "metadata": {
            "skill_check": {
                "sneak past the guard": "easy"
            }
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
            "You also spot a torn note: 'The elder is awaiting your reply.'\n\n"
            "What do you take?\n"
        ),
        "choices": {
            "go back and enter the narrow passage": "SewerEntrance",
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

    # COMBAT
    "TutorialCombat": {
        "text": (
            "You enter a small room where a training dummy stands in the center.\n"
            "A sign on the wall reads: 'Practice your combat skills here'.\n"
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
            "dodge": 10
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
        "metadata": {
            "skill_check": {
                "intimidate the guard": "medium"
            }
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
            "dodge": 10
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

# Tutorial over
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
    
    "CampfireScene": {
        "text": (
            "You creep closer to the flickering light, sticking to the shadows. As you near the campfire, "
            "you spot three bandits sitting around it, laughing and passing around a flask.\n"
            "Behind them is a weathered wooden chest and a crude map nailed to a tree.\n\n"
            "The wind shifts and carries your scent—one of the bandits pauses, sniffing the air.\n\n"
            "What do you do?\n"
        ),
        "choices": {
            "ambush them now": "BanditFight",
            "create distraction": "CampfireDistraction",
            "wait and observe": "CampfireIntel",
        },
    },

    "BanditFight": {
        "text": (
            "You leap from the underbrush, weapon drawn! The bandits scramble, drawing their blades.\n"
            "A fast and brutal skirmish begins beneath the forest canopy.\n"
        ),
        "combat": True,
        "enemy": {
            "name": "Bandit Trio",
            "hp": 70,
            "damage": 10,
        },
        "alive": True,
        "choices": {
            "search the camp": "BanditCampLoot",
        },
    },

    "CampfireDistraction": {
        "text": (
            "You throw a stone into the forest beyond the camp. One bandit stands, squinting into the darkness.\n"
            "'Go check it out,' one grumbles.\n"
            "As he walks off, the remaining two go quiet, looking nervous.\n\n"
            "You slip closer to the chest.\n"
        ),
        "choices": {
            "steal from the chest": "BanditCampLoot",
            "knock out remaining bandits": "KnockoutAttempt",
        },
    },

    "CampfireIntel": {
        "text": (
            "You stay hidden and listen.\n"
            "'The temple's just past the ridge. Elder says the relic's still inside.'\n"
            "'Yeah, and that priest keeps babbling about the gods watching us. Creepy bastard.'\n\n"
            "This could be the clue you need.\n"
        ),
        "choices": {
            "sneak away quietly": "ForestTemplePath",
            "take them by surprise": "BanditFight",
        },
        "metadata": {
            "clue": True,
        },
    },

    "KnockoutAttempt": {
        "text": (
            "You creep up behind the nearest bandit and strike — clean and silent.\n"
            "The second one turns just in time to meet your fist. They're both down.\n"
            "No alarms raised.\n"
        ),
        "choices": {
            "search the camp": "BanditCampLoot",
        },
    },

    "BanditCampLoot": {
        "text": (
            "You search the chest and find a worn map with markings leading to a 'Sunken Temple'and "
            "a strange stone pendant.\n\n"
            "You now have a heading — time to find out what's hidden in the ruins.\n"
        ),
        "choices": {
            "follow the map to the temple": "ForestTemplePath",
        },
        "metadata": {
            "items": ["temple_map", "stone_pendant",],
        },
    },

    "ForestTemplePath": {
        "text": (
            "The trees grow denser as you travel toward the marked location. Moss-covered stones emerge "
            "from the undergrowth, forming an ancient path. Birds fall silent. Something sacred — or cursed — lies ahead.\n\n"
            "The temple entrance looms up ahead, half-buried in vines.\n"
        ),
        "choices": {
            "enter the temple": "TempleEntrance",
            "inspect the area around the temple first": "TemplePerimeter",
        },
    },
    "TemplePerimeter": {
        "text": (
            "You circle the temple ruins carefully. The forest seems to hold its breath.\n"
            "Near the rear of the temple, you find a collapsed section of wall partially hidden by thick vines.\n"
            "Scratched into the stone is a symbol matching the one on your pendant — the stone faintly glows.\n\n"
            "There’s a crack just wide enough to squeeze through.\n"
        ),
        "choices": {
            "enter through the crack": "TempleInnerSanctum",
            "go back and enter via the main door": "TempleEntrance",
        },
        "metadata": {
            "skill_check": {
                "enter through the crack": "easy"
            },
            "clue": True,
        },
    },

    "TempleEntrance": {
        "text": (
            "You push open the heavy temple doors. Dust and darkness greet you.\n"
            "The air is heavy with age and incense. Faded murals line the walls — warriors kneeling before winged figures.\n"
            "An altar glows faintly at the far end, and strange chanting echoes deeper inside.\n\n"
            "What do you do?\n"
        ),
        "choices": {
            "approach the altar": "AltarInvestigation",
            "follow the sound of chanting": "CultEncounter",
        },
    },
    "CultEncounter": {
        "text": (
            "You follow the chanting deeper into the temple. The air grows thick with incense and the sound of drums.\n"
            "You find a group of hooded figures gathered around a large stone altar, chanting in an ancient tongue.\n"
            "Atop the altar lies a glowing relic, pulsating with energy.\n\n"
            "The cultists turn to you, eyes wide with surprise.\n"
        ),
        "choices": {
            "demand the relic": "RelicDemand",
            "attack the cultists": "CultistFight",
        },
    },
    "RelicDemand": {
        "text": (
            "You step forward, demanding the relic. The cultists exchange glances, then one steps forward.\n"
            "'You seek the relic? It is not for the unworthy.'\n"
            "He raises his hands, and the relic glows brighter.\n\n"
            "What do you do?\n"
        ),
        "choices": {
            "fight for the relic": "CultistFight",
            "offer to prove your worthiness": "RelicChallenge",
        },
    },
    "CultistFight": {
        "text": (
            "The cultists draw their weapons, chanting louder. You ready yourself for a fight.\n"
            "The air crackles with energy as the relic pulses on the altar.\n\n"
            "Prepare for battle!\n"
        ),
        "combat": True,
        "enemy": {
            "name": "Cultist Group",
            "hp": 50,
            "damage": 12,
        },
        "alive": True,
        "choices": {
            "search the altar after victory": "RelicAcquisition",
        },
    },
    "RelicChallenge": {
        "text": (
            "The cultist nods, intrigued. 'Very well. To prove your worth, you must answer a riddle.'\n"
            "'What is the key that opens all doors but cannot be seen?'\n\n"
            "You think carefully about the answer.\n"
        ),
        "choices": {
            "answer 'knowledge'": "RelicAcquisition",  # Correct answer
            "answer 'time'": "RelicUnworth",  # Incorrect answer leads to escape
            "refuse to answer": "RelicRefusal",  # Leads to combat
        },
    },
    "RelicAcquisition": {
        "text": (
            "The cultist nods approvingly. 'You have proven your worth.'\n"
            "He steps aside, allowing you to take the relic from the altar.\n"
            "As you grasp it, a surge of power flows through you. You feel a connection to the ancient gods.\n\n"
            "You now possess the Relic of the Gods.\n"
        ),
        "choices": {
            "leave the temple with the relic": "EndingWithRelic",
            "travel back to town with the relic": "TownReturnWithRelic",
        },
        "metadata": {
            "items": ["relic_of_the_gods"],
        },
    },
    "RelicUnworth": {
        "text": (
            "The cultist shakes his head. 'You are not worthy of the relic.'\n"
            "With a wave of his hand, the relic vanishes, and the cultists prepare to attack.\n\n"
            "You must escape!\n"
        ),
        "choices": {
            "fight your way out": "CultistFight",
            "flee the temple": "TempleEscape",
        },
    },
    "RelicRefusal": {
        "text": (
            "The cultist scowls. 'You refuse to answer? Then you are not worthy.'\n"
            "He raises his hands, and the relic glows ominously.\n"
            "The cultists prepare to attack.\n\n"
            "Prepare for battle!\n"
        ),
        "combat": True,
        "enemy": {
            "name": "Cultist Group",
            "hp": 50,
            "damage": 12,
        },
        "alive": True,
        "choices": {
            "search the altar after victory": "RelicAcquisition",
        },
    },
    "TempleEscape": {
        "text": (
            "You turn and sprint back through the temple, the cultists shouting behind you.\n"
            "You burst through the main doors and into the forest, heart pounding.\n"
            "The relic is lost, but you have escaped with your life.\n\n"
            "What will you do now?\n"
        ),
        "choices": {
            "head back to town empty-handed": "TownReturnEmpty",
        },
    },
    "AltarInvestigation": {
            "text": (
            "You step cautiously toward the altar. The stone is warm to the touch, and the faint glow intensifies as you approach.\n"
            "The altar is adorned with offerings — trinkets, bones, and a large, glowing crystal at its center.\n"
            "There is a note pinned to the altar: 'To those who seek the truth, the gods await your sacrifice.\n\n"
            "What do you do?\n"
        ),
        "choices": {
            "sacrifice an item from invenstory": "SacrificeItem", # Nothing happens
            "sacrifice yourself": "DeathEnding", # DEATH SCENE
            "sacrifice entire inventory": "GainRelicSacrifice", # You gain The Relic of the Gods
        },
    },
}