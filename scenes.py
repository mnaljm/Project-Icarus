# SCENE DATA FOR TEXT ADVENTURE GAME
# This file contains all the scenes organized in logical progression order
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

scenes = {
    # ================================
    # CHAPTER 1: PRISON ESCAPE
    # ================================
    
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

    # --- STEALTH PATH ---
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

    # --- COMBAT PATH ---
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

    # ================================
    # CHAPTER 2: THE OUTSIDE WORLD
    # ================================

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
            "head to the nearby town": "TownApproach",
        },
    },

    "ForestWander": {
        "text": (
            "You decide to avoid the campfire and head deeper into the forest.\n"
            "The trees grow thicker and the moonlight struggles to penetrate the canopy.\n"
            "After hours of walking, you stumble upon an old stone bridge crossing a dark ravine.\n"
            "Strange symbols are carved into the bridge's railings.\n\n"
            "What do you do?\n"
        ),
        "choices": {
            "cross the bridge": "ForestTemplePath",
            "turn back and look for the campfire": "CampfireScene",
        },
    },

    # --- BANDIT CAMP ENCOUNTERS ---
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
            "play a game to pass": "RPSGame",
            "create distraction": "CampfireDistraction",
            "wait and observe": "CampfireIntel",
        },
    },

    "RPSGame": {
        "text": (
            "You step out of the shadows and challange the good and honorable bandits to a game of Rock Paper Siccors,\n"
            "if you win, they'll have to let you pass?\n"
            "The bandits look at each other, confused but intrigued.\n"
            "One bandit stands up and lets out a bellow of laughter. he says,\n"
            "'all right, if you win, we'll let you go. If you lose, you give us everything you've got.'\n"
            "'Alright, stranger. Winner takes all,' one says, grinning.\n\n"
        ),
        "choices": {
            "play the game": "PlayRPS",
        },
    },
    
    "PlayRPS": {
        "text": (
            "You play a quick game with them, using your wits to outsmart the bandits.\n"
        ),
        "choices": {
            "sore losers": "BanditFightGame",
        },
        "minigame": True,
        "minigame_type": "rps",
    },

    "BanditFightGame": {
        "text": (
            "Good and honorable maybe, but they are sore losers for sure\n"
            "A fast and brutal skirmish begins beneath the forest canopy.\n"
        ),
        "combat": True,
        "enemy": {
            "name": "Bandit Trio",
            "hp": 70,
            "damage": 10,
            "dodge": 10
        },
        "alive": True,
        "choices": {
            "search the camp": "BanditCampLoot",
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
            "dodge": 10
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
            "catch them by surprise": "BanditFight",
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

    # ================================
    # CHAPTER 3: TOWN SEQUENCE
    # ================================

    "TownApproach": {
        "text": (
            "You make your way through the forest toward the faint glow of lights in the distance.\n"
            "As you emerge from the treeline, you see a small town nestled in a valley below.\n"
            "Smoke rises from chimneys and you can hear the distant sounds of people going about their evening routines.\n\n"
            "The town walls are low and the gates appear unguarded. This could be a chance to gather information and supplies.\n\n"
            "How do you approach?\n"
        ),
        "choices": {
            "sneak into town quietly": "TownStealth",
            "walk in openly through the main gate": "TownMainGate",
            "circle around to find another entrance": "TownBackEntrance",
        },
    },

    # --- TOWN ENTRY METHODS ---
    "TownStealth": {
        "text": (
            "You wait until full darkness and slip over the town wall where it's lowest.\n"
            "You find yourself in a narrow alley behind some shops, the smell of bread and ale drifting from nearby establishments.\n"
            "Most people have retired for the evening, but you can see light coming from a tavern and hear muffled conversation.\n\n"
            "Where do you go first?\n"
        ),
        "choices": {
            "investigate the tavern": "TownTavern",
            "explore the shops": "TownShops",
            "look for the town center": "TownCenter",
        },
    },

    "TownMainGate": {
        "text": (
            "You walk confidently toward the main gate, hoping your prison clothes aren't too obvious in the darkness.\n"
            "A single guard sits by a small fire, half-asleep. He glances up as you approach.\n"
            "'Evening, stranger. Bit late to be traveling, isn't it?'\n\n"
            "How do you respond?\n"
        ),
        "choices": {
            "claim to be a traveling merchant": "TownMerchantLie",
            "say you're seeking shelter": "TownShelterRequest",
            "offer the guard a bribe": "TownBribeGuard",
        },
    },

    "TownBackEntrance": {
        "text": (
            "You circle the town and find a small service gate near what looks like a market area.\n"
            "The gate is unlocked and opens with a soft creak. You slip inside and find yourself among merchant stalls and wagons.\n"
            "The market is empty at this hour, but you notice a few late-night establishments still open.\n\n"
            "What catches your attention?\n"
        ),
        "choices": {
            "examine the merchant stalls": "TownMarketStalls",
            "head toward the lighted buildings": "TownNightEstablishments",
            "look for a place to rest": "TownRestSearch",
        },
    },

    # --- GUARD INTERACTIONS ---
    "TownMerchantLie": {
        "text": (
            "You tell the guard you're a traveling merchant whose wagon broke down nearby.\n"
            "He eyes you suspiciously but seems too tired to investigate further.\n"
            "'Alright, but no trouble. Town's had enough problems lately with all the bandit activity.'\n"
            "He waves you through. You're now in the main square of the town.\n"
        ),
        "choices": {
            "ask the guard about the bandit activity": "TownGuardInfo",
            "head into the town square": "TownCenter",
        },
        "metadata": {
            "clue": True,
        },
    },

    "TownShelterRequest": {
        "text": (
            "You explain that you're a weary traveler seeking shelter for the night.\n"
            "The guard softens a bit. 'Aye, it's dangerous on the roads these days. Try the Sleeping Dragon inn.'\n"
            "He points toward a building with a wooden dragon sign hanging outside.\n"
            "You thank him and enter the town.\n"
        ),
        "choices": {
            "go to the Sleeping Dragon inn": "TownInn",
            "explore the town first": "TownCenter",
        },
    },

    "TownBribeGuard": {
        "text": (
            "You discreetly offer the guard a coin from your pocket.\n"
            "His eyes light up and he pockets it quickly. 'Much appreciated, friend.'\n"
            "'Word of advice - avoid the temple district tonight. Strange happenings there lately.'\n"
            "Interesting information. You enter the town.\n"
        ),
        "choices": {
            "ask about the temple district": "TownTempleInfo",
            "explore the main town": "TownCenter",
        },
        "metadata": {
            "clue": True,
        },
    },

    "TownGuardInfo": {
        "text": (
            "The guard tells you about increased bandit activity near the old temple.\n"
            "'Strange things happening out there. People going missing.'\n"
        ),
        "choices": {
            "ask about the temple": "TownTempleInfo",
            "head into town": "TownCenter",
        },
        "metadata": {
            "clue": True,
        },
    },

    # --- TOWN CENTER AND EXPLORATION ---
    "TownCenter": {
        "text": (
            "You find yourself in the town's main square. A stone fountain sits in the center.\n"
            "You see the Sleeping Dragon inn with warm light spilling from its windows,\n"
            "a general store that's closed, and a small temple at the far end.\n"
            "A few people still move about despite the late hour.\n"
        ),
        "choices": {
            "enter the Sleeping Dragon inn": "TownInn",
            "investigate the temple": "TownTemple",
            "listen to conversations in the square": "TownGossip",
        },
    },

    "TownGossip": {
        "text": (
            "You listen to the conversations around the square.\n"
            "People are talking about strange lights in the forest and missing travelers.\n"
            "Most interesting is mention of an old temple that's become active again.\n"
        ),
        "choices": {
            "ask someone about the temple": "TownTempleInfo",
            "head to the inn for more information": "TownInn",
        },
        "metadata": {
            "clue": True,
        },
    },

    # --- INN AND TAVERN ---
    "TownInn": {
        "text": (
            "You push open the heavy door of the Sleeping Dragon inn. The warmth and noise hit you immediately.\n"
            "The innkeeper, a stout woman with graying hair, approaches you.\n"
            "'Welcome to the Dragon, stranger. You look like you've had a rough journey.'\n"
        ),
        "choices": {
            "ask for a room for the night": "TownRoom",
            "order food and listen to conversations": "TownIntelGathering",
            "ask the innkeeper about local news": "TownNews",
            "You see a man in the corner with a set of dice, he seems to be looking for a game": "TownDiceGame",
        },
    },

    "TownDiceGame": {
        "text": (
            "You approach the man with the dice. He looks up and grins.\n"
            "'Fancy a game? I could use a good challenge.'\n"
            "He rolls the dice in his hand, the sound of clattering bone echoing in the inn.\n"
            "'Let's make it interesting. I won't tell the guards about you if you win, if I win you have to leave town.'\n"
        ),
        "choices": {
            "accept the challenge": "DiceGameChallenge",
            "politely decline": "TownIntelGathering",
        },
    },

    "DiceGameChallenge": {
        "text": (
            "You nod and take a seat at his table. He explains the rules of the game, which involve rolling dice to match certain numbers.\n"
            "You both roll, and the tension in the air is palpable as you try to outsmart each other.\n"
        ),
        "minigame": True,
        "minigame_type": "dice_poker",
        "choices": {
            "Thank him for the game": "TownTavern"
        },
    },
    "TownTavern": {
        "text": (
            "You approach the tavern and peer through a window. Inside, you see several patrons drinking.\n"
            "You catch fragments of conversation: '...temple in the woods...' and '...Elder's men were here again...'\n"
            "Do you go inside?\n"
        ),
        "choices": {
            "enter the tavern": "TownInn",
            "listen from outside longer": "TownGossip",
            "move on to explore elsewhere": "TownShops",
        },
        "metadata": {
            "clue": True,
        },
    },

    "TownRoom": {
        "text": (
            "The innkeeper quotes you a reasonable price for a small room upstairs.\n"
            "You pay and she hands you a key.\n"
            "'Sleep well - and if you hear anything strange in the night, just ignore it.'\n"
        ),
        "choices": {
            "ask about the strange sounds": "TownTempleInfo",
            "go to your room to rest": "TownRest",
            "stay downstairs to gather information": "TownIntelGathering",
        },
    },

    "TownIntelGathering": {
        "text": (
            "You order a meal and ale, then find a corner table where you can listen to conversations.\n"
            "Over the course of an hour, you piece together several important facts:\n"
            "- Strange lights have been seen near an ancient temple in the forest\n"
            "- The Elder's bandits have been more active lately\n"
            "- Several townspeople have gone missing\n"
        ),
        "choices": {
            "prepare to leave for the temple": "TownLeaveForTemple",
            "get a room for the night": "TownRoom",
        },
        "metadata": {
            "clue": True,
        },
    },

    "TownNews": {
        "text": (
            "The innkeeper leans in conspiratorially.\n"
            "'Well, since you seem like a decent sort... there's been strange doings lately.'\n"
            "'People going missing, weird lights in the forest, and that old temple has been drawing unsavory types.'\n"
        ),
        "choices": {
            "ask about the temple specifically": "TownTempleInfo",
            "thank her and order a room": "TownRoom",
        },
        "metadata": {
            "clue": True,
        },
    },

    "TownRest": {
        "text": (
            "You spend the night in the inn, getting much-needed rest after your escape from prison.\n"
            "In the morning, you feel refreshed and ready for whatever lies ahead.\n"
            "You're now ready to leave town for the temple.\n"
        ),
        "choices": {
            "gather final supplies": "TownShops",
            "head directly to the temple": "TownLeaveForTemple",
        },
    },

    # --- TEMPLE INFORMATION ---
    "TownTempleInfo": {
        "text": (
            "When you ask about the temple, the person becomes visibly uncomfortable.\n"
            "'The old temple in the woods? That place has been abandoned for generations... until recently.'\n"
            "'Now there's cultists or something up there, performing rituals.'\n"
        ),
        "choices": {
            "ask for directions to the temple": "TownTempleDirections",
            "thank them and move on": "TownCenter",
        },
        "metadata": {
            "clue": True,
        },
    },

    "TownTempleDirections": {
        "text": (
            "'You're not actually thinking of going there, are you?' they ask with concern.\n"
            "When you insist, they reluctantly provide directions:\n"
            "'Follow the old merchant road north for about two miles, then look for the stone markers.'\n"
            "You now have clear directions to the temple.\n"
        ),
        "choices": {
            "gather supplies before leaving": "TownShops",
            "leave immediately for the temple": "TownLeaveForTemple",
        },
        "metadata": {
            "items": ["temple_directions"],
        },
    },

    "TownTemple": {
        "text": (
            "You approach the small town temple. It's modest compared to the ancient temple in the forest.\n"
            "A priest is inside, praying by candlelight. He looks up as you enter.\n"
            "'Welcome, traveler. You look troubled. Perhaps you seek guidance?'\n"
        ),
        "choices": {
            "ask about the forest temple": "TownTempleInfo",
            "request a blessing": "TownBlessing",
            "leave quietly": "TownCenter",
        },
    },

    "TownBlessing": {
        "text": (
            "The priest performs a simple blessing over you.\n"
            "'May the light protect you from the darkness ahead. I sense you face great trials.'\n"
            "You feel a sense of peace and protection.\n"
        ),
        "choices": {
            "ask about the forest temple": "TownTempleInfo",
            "thank him and leave": "TownCenter",
        },
        "metadata": {
            "items": ["priests_blessing"],
        },
    },

    # --- SHOPPING AND SUPPLIES ---
    "TownShops": {
        "text": (
            "You check the general store, but it's closed for the night.\n"
            "However, you notice a small black market operation running out of an alley behind the inn.\n"
            "A shifty-looking merchant offers various supplies.\n"
            "'Need anything for the road, friend? I've got provisions, tools, even some protection.'\n"
        ),
        "choices": {
            "buy travel provisions": "TownBuyProvisions",
            "ask about weapons or protective gear": "TownBuyWeapons",
            "decline and move on": "TownCenter",
        },
    },

    "TownBuyProvisions": {
        "text": (
            "You purchase some basic travel supplies - dried food, water, rope, and a small lantern.\n"
            "The merchant throws in a map of the local area.\n"
            "You're now better equipped for the journey ahead.\n"
        ),
        "choices": {
            "head to the temple": "TownLeaveForTemple",
            "find a place to rest first": "TownRoom",
        },
        "metadata": {
            "items": ["travel_supplies", "local_map"],
        },
    },

    "TownBuyWeapons": {
        "text": (
            "The merchant shows you a selection of basic weapons and armor.\n"
            "You select a sturdy knife and a leather vest that offers some protection.\n"
            "You feel more prepared for danger.\n"
        ),
        "choices": {
            "buy provisions as well": "TownBuyProvisions",
            "leave for the temple": "TownLeaveForTemple",
        },
        "metadata": {
            "items": ["sturdy_knife", "leather_vest"],
        },
    },

    # --- MINOR TOWN SCENES ---
    "TownMarketStalls": {
        "text": (
            "You examine the merchant stalls but find nothing of immediate use.\n"
            "Most are locked up for the night, though you do find some basic supplies.\n"
        ),
        "choices": {
            "head to the lighted buildings": "TownCenter",
        },
    },

    "TownNightEstablishments": {
        "text": (
            "You head toward the lighted buildings and find yourself at the town center.\n"
        ),
        "choices": {
            "explore the main square": "TownCenter",
        },
    },

    "TownRestSearch": {
        "text": (
            "You look for a place to rest and notice the Sleeping Dragon inn is still open.\n"
        ),
        "choices": {
            "go to the inn": "TownInn",
        },
    },

    "TownLeaveForTemple": {
        "text": (
            "You leave the town behind and head toward the forest temple.\n"
            "Armed with information, supplies, and a clearer understanding of what awaits you,\n"
            "you feel more prepared for the challenges ahead.\n"
            "The forest looms before you, and somewhere within it lies the temple and its secrets.\n"
        ),
        "choices": {
            "follow the directions to the temple": "ForestTemplePath",
            "explore the forest first": "ForestWander",
        },
    },

    # ================================
    # CHAPTER 4: THE TEMPLE APPROACH
    # ================================

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
            "There's a crack just wide enough to squeeze through.\n"
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

    # ================================
    # CHAPTER 5: INSIDE THE TEMPLE
    # ================================

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

    "TempleInnerSanctum": {
        "text": (
            "You squeeze through the crack in the wall and find yourself in a hidden chamber.\n"
            "The room is filled with ancient artifacts and glowing crystals embedded in the walls.\n"
            "At the center stands a pedestal with the same relic you saw the cultists worshipping.\n"
            "Unlike the main chamber, this place feels peaceful, untouched by the cultists.\n\n"
            "The pendant around your neck pulses in harmony with the relic.\n"
        ),
        "choices": {
            "grab the relic": "RelicAcquisition",
            "examine the artifacts first": "SanctumExploration",
        },
        "metadata": {
            "items": ["ancient_scroll"],
        },
    },

    "SanctumExploration": {
        "text": (
            "You examine the ancient artifacts scattered around the chamber.\n"
            "Among them, you find scrolls detailing the history of the relic and its connection to the old gods.\n"
            "The knowledge fills you with understanding of the relic's true power.\n\n"
            "With this wisdom, you approach the pedestal.\n"
        ),
        "choices": {
            "grab the relic with newfound knowledge": "RelicAcquisition",
        },
        "metadata": {
            "items": ["ancient_knowledge"],
            "clue": True,
        },
    },

    # --- ALTAR PATH ---
    "AltarInvestigation": {
        "text": (
            "You step cautiously toward the altar. The stone is warm to the touch, and the faint glow intensifies as you approach.\n"
            "The altar is adorned with offerings — trinkets, bones, and a large, glowing crystal at its center.\n"
            "There is a note pinned to the altar: 'To those who seek the truth, the gods await your sacrifice.'\n\n"
            "What do you do?\n"
        ),
        "choices": {
            "sacrifice an item from inventory": "SacrificeItem",
            "sacrifice yourself": "DeathEnding",
            "sacrifice entire inventory": "GainRelicSacrifice",
        },
    },

    "SacrificeItem": {
        "text": (
            "You place one of your items on the altar as an offering.\n"
            "The altar glows briefly, but nothing significant happens.\n"
            "The gods seem to require a greater sacrifice.\n\n"
            "What will you do next?\n"
        ),
        "choices": {
            "sacrifice your entire inventory": "GainRelicSacrifice",
            "sacrifice yourself": "DeathEnding",
            "leave the altar and explore elsewhere": "CultEncounter",
        },
    },

    "GainRelicSacrifice": {
        "text": (
            "You place all your possessions on the altar as an offering to the gods.\n"
            "The altar erupts in brilliant light, and your items are untouched by the divine fire.\n"
            "In return, for your trust the gods grant you the Relic of the Gods, its power now bound to your soul.\n\n"
            "You feel the weight of divine responsibility upon you.\n"
        ),
        "choices": {
            "leave the temple as a chosen one": "EndingWithRelic",
            "stay and commune with the gods": "DivineEnding",
        },
        "metadata": {
            "items": ["relic_of_the_gods"],
        },
    },

    # --- CULTIST PATH ---
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

    "RelicChallenge": {
        "text": (
            "The cultist nods, intrigued. 'Very well. To prove your worth, you must answer a riddle.'\n"
            "'What is the key that opens all doors but cannot be seen?'\n\n"
            "You think carefully about the answer.\n"
        ),
        "choices": {
            "answer 'knowledge'": "RelicAcquisition",
            "answer 'time'": "RelicUnworth",
            "refuse to answer": "RelicRefusal",
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
            "dodge": 10
        },
        "alive": True,
        "choices": {
            "search the altar after victory": "RelicAcquisition",
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
            "dodge": 10
        },
        "alive": True,
        "choices": {
            "search the altar after victory": "RelicAcquisition",
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

    # --- RELIC ACQUISITION ---
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

    # ================================
    # CHAPTER 6: ENDINGS
    # ================================

    "DeathEnding": {
        "text": (
            "You decide to make the ultimate sacrifice and offer yourself to the gods.\n"
            "As you step onto the altar, a blinding light engulfs you.\n"
            "Your consciousness fades as you feel your essence being absorbed by the ancient powers.\n\n"
            "THE END - [SACRIFICIAL DEATH]"
        ),
        "choices": {},
    },

    "DivineEnding": {
        "text": (
            "You remain at the altar, feeling the presence of the ancient gods.\n"
            "They speak to you in whispers, revealing the cosmic truth of existence.\n"
            "You become their earthly vessel, forever bound to serve the divine will.\n\n"
            "THE END - [DIVINE ASCENSION]"
        ),
        "choices": {},
    },

    "EndingWithRelic": {
        "text": (
            "You emerge from the temple, the Relic of the Gods in your possession.\n"
            "Its power courses through you, granting you abilities beyond mortal understanding.\n"
            "The forest seems to recognize your new status, and even the darkness bows before you.\n\n"
            "You walk into the night, ready to reshape the world with divine power.\n\n"
            "THE END - [RELIC MASTER]"
        ),
        "choices": {},
    },

    "TownReturnWithRelic": {
        "text": (
            "You return to the town with the Relic of the Gods in your possession.\n"
            "The townspeople gather around you, sensing the divine power you now wield.\n"
            "Some kneel in reverence, others flee in terror.\n"
            "You have become something more than human.\n\n"
            "With the relic's power, you establish yourself as the town's new spiritual leader.\n\n"
            "THE END - [DIVINE RULER]"
        ),
        "choices": {},
    },

    "TownReturnEmpty": {
        "text": (
            "You make your way back to town, exhausted and empty-handed.\n"
            "The prison break seems like a lifetime ago, and you've learned much about the world's hidden mysteries.\n"
            "Though you didn't claim the relic, you survived encounters with cultists and ancient powers.\n\n"
            "You slip into the town under cover of darkness, ready to start a new life in the shadows.\n\n"
            "THE END - [SURVIVOR'S ESCAPE]"
        ),
        "choices": {},
    },
}
