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
    "opening": {
        "text": (
            "🌅 The Mysterious Island\n\n"
            "You wake up on a sandy beach, the sun beating down on your face. "
            "The last thing you remember is the storm that wrecked your small boat. "
            "Salt water stings your eyes as you sit up and look around.\n\n"
            "To your left, you see a dense jungle with strange sounds echoing from within. "
            "To your right, there are rocky cliffs with what appears to be a cave entrance. "
            "Straight ahead, the ocean stretches endlessly to the horizon.\n\n"
            "What do you do first?\n"
            "(explore jungle/investigate cave/search beach)\n"
        ),
        "choices": {
            "explore jungle": "jungle_entrance",
            "investigate cave": "cave_entrance", 
            "search beach": "beach_search"
        },
        "metadata": {
            "location": "shipwreck_beach",
            "items": [],
            "npcs": [],
            "visited": False
        }
    },

    "jungle_entrance": {
        "text": (
            "🌿 Into the Green Unknown\n\n"
            "You push through the thick foliage at the jungle's edge. Vines hang like "
            "curtains, and exotic birds call out from the canopy above. The air is "
            "humid and thick with the scent of rotting vegetation.\n\n"
            "After walking for several minutes, you come to a fork in the path. "
            "To the left, you hear the sound of running water. To the right, "
            "you notice carved stone markers partially hidden by moss.\n\n"
            "A rustling in the bushes behind you suggests something might be following.\n\n"
            "Which path do you take?\n"
            "(follow water sounds/examine stone markers/turn back)\n"
        ),
        "choices": {
            "follow water sounds": "jungle_stream",
            "examine stone markers": "ancient_ruins",
            "turn back": "opening"
        },
        "metadata": {
            "location": "jungle_path",
            "items": [],
            "npcs": [],
            "visited": False
        }
    },

    "cave_entrance": {
        "text": (
            "🪨 The Dark Depths\n\n"
            "You climb carefully over the rocky terrain toward the cave. The entrance "
            "is larger than it appeared from the beach - easily tall enough for you "
            "to walk through without ducking.\n\n"
            "Cool air flows out from the darkness within, bringing with it a strange "
            "metallic scent. As your eyes adjust, you can make out two passages "
            "branching off from the main cavern.\n\n"
            "Old torch brackets are mounted on the walls, though they've been empty "
            "for what looks like decades. You notice fresh footprints in the sandy "
            "cave floor - someone else has been here recently.\n\n"
            "What's your next move?\n"
            "(enter left passage/enter right passage/return to beach)\n"
        ),
        "choices": {
            "enter left passage": "cave_left",
            "enter right passage": "cave_right",
            "return to beach": "opening"
        },
        "metadata": {
            "location": "cave_entrance",
            "items": ["torch_bracket"],
            "npcs": [],
            "visited": False
        }
    },

    "beach_search": {
        "text": (
            "🏖️ Combing the Shore\n\n"
            "You decide to thoroughly search the beach before venturing elsewhere. "
            "Walking along the waterline, you find pieces of your boat scattered "
            "across the sand - a broken mast, some rope, and part of the hull.\n\n"
            "But more interesting are the other things you discover: an old glass "
            "bottle with something inside, half-buried metal objects that look "
            "like coins, and what appears to be a leather journal wrapped in "
            "oiled cloth.\n\n"
            "As you examine your findings, you notice smoke rising from somewhere "
            "deeper inland. Someone else is on this island!\n\n"
            "What do you investigate first?\n"
            "(open bottle/examine coins/read journal/follow smoke)\n"
        ),
        "choices": {
            "open bottle": "message_bottle",
            "examine coins": "ancient_coins",
            "read journal": "old_journal", 
            "follow smoke": "smoke_source"
        },
        "metadata": {
            "location": "shipwreck_beach",
            "items": ["glass_bottle", "ancient_coins", "leather_journal"],
            "npcs": [],
            "visited": False
        }
    },

    "jungle_stream": {
        "text": (
            "💧 The Hidden Oasis\n\n"
            "Following the sound of water, you push through hanging vines and find "
            "yourself at the edge of a beautiful hidden pool. Crystal clear water "
            "cascades down from rocks above, creating a natural swimming hole.\n\n"
            "But you're not alone. An elderly man sits beside the pool, fishing "
            "with a makeshift rod. He looks up as you approach, his weathered face "
            "breaking into a knowing smile.\n\n"
            "'Ah, another one washes ashore,' he says calmly. 'Been expecting you, "
            "young one. This island has a way of calling to those who need to find "
            "something - or lose something.'\n\n"
            "How do you respond?\n"
            "(ask about the island/ask about other survivors/ask about escape)\n"
        ),
        "choices": {
            "ask about the island": "island_secrets",
            "ask about other survivors": "other_survivors",
            "ask about escape": "escape_attempt"
        },
        "metadata": {
            "location": "hidden_oasis",
            "items": ["fresh_water"],
            "npcs": ["old_fisherman"],
            "visited": False
        }
    },

    "ancient_ruins": {
        "text": (
            "🏛️ Echoes of the Past\n\n"
            "The stone markers lead you to a clearing where ancient ruins emerge "
            "from the jungle floor. Crumbling stone structures covered in intricate "
            "carvings stretch out before you. This civilization must be hundreds, "
            "maybe thousands of years old.\n\n"
            "In the center of the ruins stands a stone pedestal with a crystal "
            "formation that seems to pulse with its own inner light. Strange "
            "symbols are carved around its base.\n\n"
            "As you approach, you feel a strange energy in the air. The crystal "
            "grows brighter, and you hear a low humming sound that seems to "
            "resonate in your bones.\n\n"
            "What do you do?\n"
            "(touch the crystal/study the symbols/leave immediately)\n"
        ),
        "choices": {
            "touch the crystal": "crystal_power",
            "study the symbols": "ancient_knowledge",
            "leave immediately": "jungle_entrance"
        },
        "metadata": {
            "location": "ancient_ruins",
            "items": ["glowing_crystal", "stone_tablets"],
            "npcs": [],
            "visited": False
        }
    },

    "message_bottle": {
        "text": (
            "📜 A Message from the Past\n\n"
            "You carefully work the cork from the old bottle. Inside is a rolled "
            "piece of parchment, surprisingly well preserved. As you unroll it, "
            "you see it's a map of the island with several locations marked.\n\n"
            "The map shows your current beach, but also reveals a hidden harbor "
            "on the other side of the island, ancient ruins in the jungle center, "
            "and something called 'The Watcher's Tower' at the island's highest point.\n\n"
            "At the bottom of the map, a note reads: 'To those who follow - "
            "The island keeps its secrets well, but rewards those who seek truth. "
            "Beware the choices you make, for some paths lead to wonder, "
            "others to sorrow. - Captain E. Morgan, 1847'\n\n"
            "Armed with this knowledge, where do you go?\n"
            "(seek the hidden harbor/head to ruins/climb to tower)\n"
        ),
        "choices": {
            "seek the hidden harbor": "hidden_harbor",
            "head to ruins": "ancient_ruins",
            "climb to tower": "watchers_tower"
        },
        "metadata": {
            "location": "shipwreck_beach",
            "items": ["treasure_map"],
            "npcs": [],
            "visited": False
        }
    },

    "island_secrets": {
        "text": (
            "🌴 The Island's Truth\n\n"
            "The old fisherman nods thoughtfully. 'This island... it's not like others. "
            "Been here forty years now, and I've seen things that would make most "
            "folks question their sanity.'\n\n"
            "He gestures toward the jungle. 'The ruins you might find - they're older "
            "than any civilization we know. And that crystal at their heart? It's "
            "been calling to shipwrecked souls for centuries.'\n\n"
            "'Some say the island exists between worlds, a place where reality bends. "
            "Those who embrace its mysteries find peace and purpose. Those who fight "
            "it...' He shakes his head sadly. 'Well, they usually don't last long.'\n\n"
            "'But you seem different. You have the look of someone who could become "
            "a true guardian of this place. What do you say?'\n\n"
            "How do you respond?\n"
            "(accept guardianship/ask for more time/refuse and seek escape)\n"
        ),
        "choices": {
            "accept guardianship": "guardian_ending",
            "ask for more time": "jungle_stream",
            "refuse and seek escape": "escape_attempt"
        },
        "metadata": {
            "location": "hidden_oasis",
            "items": [],
            "npcs": ["old_fisherman"],
            "visited": False
        }
    },

    "crystal_power": {
        "text": (
            "✨ The Crystal's Gift\n\n"
            "The moment your hand touches the crystal, the world explodes into "
            "brilliant light. But instead of pain, you feel an incredible surge "
            "of knowledge and understanding flooding your mind.\n\n"
            "Visions flash before your eyes: the ancient civilization that built "
            "these ruins, their connection to forces beyond the physical world, "
            "and the truth about this island as a nexus between dimensions.\n\n"
            "You see yourself as you truly are - not a castaway, but someone "
            "chosen to become the next guardian of this sacred place. The crystal "
            "has awakened abilities within you that you never knew existed.\n\n"
            "As the light fades, you find yourself transformed. You understand "
            "your purpose now, and feel a deep connection to the island and all "
            "its secrets. You are no longer lost - you are exactly where you "
            "belong.\n\n"
            "THE END - The Crystal Guardian\n\n"
            "🎊 You have achieved the Mystical Ending! 🎊\n"
            "Through embracing the unknown, you've found your true calling."
        ),
        "choices": {},
        "metadata": {
            "location": "ancient_ruins",
            "ending_type": "mystical",
            "items": [],
            "npcs": []
        }
    },

    "guardian_ending": {
        "text": (
            "🌅 A New Beginning\n\n"
            "You nod slowly, feeling the rightness of the decision in your heart. "
            "The old fisherman smiles and extends his hand.\n\n"
            "'Welcome, new guardian. I've been waiting decades to pass this "
            "responsibility to worthy hands.' As you shake his hand, you feel "
            "a warm energy transfer between you.\n\n"
            "Over the following days, he teaches you the island's secrets: how "
            "to read the signs in the crystal's light, how to help other castaways "
            "find their path, and how to maintain the balance between worlds.\n\n"
            "Years pass peacefully. You've helped dozens of lost souls find their "
            "way - some choosing to stay and find peace, others gaining the strength "
            "to return to their old lives. You've found a contentment here that "
            "you never knew in your previous life.\n\n"
            "THE END - The Peaceful Guardian\n\n"
            "🎊 You have achieved the Wisdom Ending! 🎊\n"
            "Through service to others, you've found true fulfillment."
        ),
        "choices": {},
        "metadata": {
            "location": "hidden_oasis", 
            "ending_type": "wisdom",
            "items": [],
            "npcs": ["old_fisherman"]
        }
    },

    "escape_attempt": {
        "text": (
            "⛵ Against the Tide\n\n"
            "Determined to return to your old life, you spend weeks building a "
            "makeshift raft from debris and jungle materials. The old fisherman "
            "watches sadly but doesn't try to stop you.\n\n"
            "'The island only keeps those who choose to stay,' he says as you "
            "prepare to launch. 'But remember - you can always come back if the "
            "outside world doesn't feel like home anymore.'\n\n"
            "Your journey across the ocean is harrowing but successful. You're "
            "rescued by a passing ship and returned to civilization. Yet in the "
            "months that follow, you find yourself constantly dreaming of the "
            "island, the crystal's light, and the peace you felt there.\n\n"
            "One day, you make a choice. You charter a boat and return to the "
            "island, ready to embrace your true destiny as its guardian.\n\n"
            "THE END - The Reluctant Return\n\n"
            "🎊 You have achieved the Journey Ending! 🎊\n"
            "Sometimes we must leave to understand what we've truly found."
        ),
        "choices": {},
        "metadata": {
            "location": "open_ocean",
            "ending_type": "journey", 
            "items": [],
            "npcs": []
        }
    },

    "hidden_harbor": {
        "text": (
            "⚓ The Secret Harbor\n\n"
            "Following the map, you trek across the island and discover a hidden "
            "cove completely concealed from the open ocean. Here, nestled between "
            "towering cliffs, is a natural harbor containing the remnants of "
            "several old ships.\n\n"
            "But one vessel catches your attention - a sleek sailing ship that "
            "looks remarkably well-preserved. As you board it, you find supplies, "
            "navigation equipment, and a logbook detailing successful escapes "
            "from the island.\n\n"
            "However, the final entry gives you pause: 'The island let me go "
            "because I understood its gift. Those who take only what they need "
            "and leave something of value in return will find favorable winds. "
            "Those who seek to plunder will find only storms.'\n\n"
            "Looking around the harbor, you notice a small shrine where previous "
            "escapees have left offerings - personal items, carved tokens, "
            "written promises.\n\n"
            "What do you leave as your offering?\n"
            "(a personal memory/a promise to return/nothing - just leave)\n"
        ),
        "choices": {
            "a personal memory": "honorable_escape",
            "a promise to return": "promised_return",
            "nothing - just leave": "stormy_departure"
        },
        "metadata": {
            "location": "hidden_harbor",
            "items": ["sailing_ship", "navigation_tools"],
            "npcs": [],
            "visited": False
        }
    },

    "cave_left": {
        "text": (
            "🕳️ The Underground River\n\n"
            "The left passage leads you deeper into the cave system. After several "
            "minutes of careful navigation, you hear the sound of rushing water. "
            "The passage opens into a vast underground cavern with a river flowing "
            "through it.\n\n"
            "On the far side of the river, you can see another passage, but the "
            "water runs swift and deep. However, you notice an old rope bridge "
            "spanning the water, though it looks quite worn.\n\n"
            "As you consider your options, you spot something glinting in the "
            "shallow water near the shore - it might be valuable.\n\n"
            "What do you do?\n"
            "(cross the rope bridge/investigate the glinting object/return to cave entrance)\n"
        ),
        "choices": {
            "cross the rope bridge": "cave_depths",
            "investigate the glinting object": "underwater_treasure",
            "return to cave entrance": "cave_entrance"
        },
        "metadata": {
            "location": "underground_river",
            "items": ["old_rope_bridge"],
            "npcs": [],
            "visited": False
        }
    },

    "cave_right": {
        "text": (
            "⭐ The Crystal Chamber\n\n"
            "The right passage winds upward, and soon you notice a faint glow "
            "emanating from ahead. The passage opens into a breathtaking chamber "
            "filled with natural crystal formations that emit their own soft light.\n\n"
            "But this isn't just a natural wonder - ancient carvings cover the walls, "
            "and in the center of the chamber sits a meditation circle made of "
            "polished stones. This place feels sacred, powerful.\n\n"
            "As you step into the circle, you feel a profound sense of peace wash "
            "over you. The crystals pulse gently, as if responding to your presence. "
            "You sense that this place could grant you great insight - or great "
            "responsibility.\n\n"
            "How do you proceed?\n"
            "(meditate in the circle/study the wall carvings/leave respectfully)\n"
        ),
        "choices": {
            "meditate in the circle": "spiritual_awakening",
            "study the wall carvings": "ancient_knowledge",
            "leave respectfully": "cave_entrance"
        },
        "metadata": {
            "location": "crystal_chamber",
            "items": ["meditation_stones", "crystal_formations"],
            "npcs": [],
            "visited": False
        }
    },

    "ancient_coins": {
        "text": (
            "🪙 Treasures of the Past\n\n"
            "Brushing the sand away, you uncover a collection of old coins unlike "
            "any you've seen before. They're made of an unusual metal that doesn't "
            "seem to tarnish, and bear symbols that match those you might find "
            "in the island's ruins.\n\n"
            "One coin is particularly intriguing - it's warm to the touch and seems "
            "to point in a specific direction, like a compass. When you hold it up, "
            "it points toward the jungle interior.\n\n"
            "You realize these aren't just old coins - they're artifacts from the "
            "ancient civilization that once inhabited this island. The compass coin "
            "might lead you to something important.\n\n"
            "What do you do with this discovery?\n"
            "(follow the compass coin/examine other beach items/keep searching the shore)\n"
        ),
        "choices": {
            "follow the compass coin": "ancient_ruins",
            "examine other beach items": "beach_search",
            "keep searching the shore": "hidden_cache"
        },
        "metadata": {
            "location": "shipwreck_beach",
            "items": ["ancient_compass_coin", "mysterious_coins"],
            "npcs": [],
            "visited": False
        }
    },

    "old_journal": {
        "text": (
            "📖 Captain's Log\n\n"
            "The leather journal belongs to Captain Elena Morgan, and as you read "
            "her entries, a fascinating story unfolds. She writes of discovering "
            "this island during a storm in 1847, much like your own experience.\n\n"
            "'Day 23: The island reveals its secrets slowly. The natives spoke of "
            "a guardian spirit that tests visitors. Those found worthy are granted "
            "great gifts. Those found wanting... well, many ships lie beneath "
            "these waters.'\n\n"
            "'Day 45: I understand now. The island doesn't trap people - it offers "
            "them a choice. I could leave with treasure enough to live like a queen, "
            "or stay and become something more. The crystal showed me possibilities "
            "I never dreamed of.'\n\n"
            "The final entry is telling: 'I've made my choice. For those who follow, "
            "know that the island's gifts are real, but they come with responsibility. "
            "Choose wisely.'\n\n"
            "What does this revelation inspire you to do?\n"
            "(seek the crystal she mentioned/look for her treasure/search for more clues)\n"
        ),
        "choices": {
            "seek the crystal she mentioned": "ancient_ruins",
            "look for her treasure": "hidden_cache",
            "search for more clues": "beach_search"
        },
        "metadata": {
            "location": "shipwreck_beach",
            "items": ["captain_journal"],
            "npcs": [],
            "visited": False
        }
    },

    "smoke_source": {
        "text": (
            "🔥 The Hermit's Camp\n\n"
            "Following the smoke trail inland, you discover a small clearing with "
            "a well-maintained campfire and simple shelter. An elderly woman tends "
            "the fire, her gray hair tied back and her clothes practical but clean.\n\n"
            "She looks up as you approach, showing no surprise at your appearance. "
            "'Another soul finds their way to my fire,' she says with a gentle smile. "
            "'I'm Sarah. Been living on this island for... oh, must be fifteen years now.'\n\n"
            "'Used to be a marine biologist before I washed up here. Now I'm... "
            "something else entirely. The island has a way of showing you what you "
            "truly are, beneath all the roles society gives you.'\n\n"
            "She offers you some fish cooking over the fire. 'You must be hungry. "
            "And I imagine you have questions.'\n\n"
            "What do you ask her?\n"
            "(how did you survive here/why didn't you try to leave/what is this place really)\n"
        ),
        "choices": {
            "how did you survive here": "survival_wisdom",
            "why didn't you try to leave": "island_calling",
            "what is this place really": "island_truth"
        },
        "metadata": {
            "location": "hermit_camp",
            "items": ["campfire", "fresh_fish"],
            "npcs": ["sarah_the_hermit"],
            "visited": False
        }
    },

    "other_survivors": {
        "text": (
            "👥 The Island's Children\n\n"
            "The old fisherman chuckles softly. 'Oh, there have been many over the "
            "years. Some choose to stay, like myself and Sarah - you might meet her "
            "if you explore the island. Others find what they came for and leave.'\n\n"
            "'There was Captain Morgan, way back. She stayed for two years, learned "
            "all the island's secrets, then sailed away with purpose in her heart. "
            "And young Marcus, the artist - he painted the most beautiful murals "
            "in the caves before moving on.'\n\n"
            "'But here's the thing - everyone who comes here was meant to come here. "
            "The island doesn't call randomly. It calls to those ready for change, "
            "ready to discover who they really are beneath all the masks they wear.'\n\n"
            "He fixes you with a knowing look. 'So the real question is - what "
            "brought you here? What were you running from, or running toward?'\n\n"
            "How do you answer?\n"
            "(I was running from my old life/I was searching for something/I don't know yet)\n"
        ),
        "choices": {
            "I was running from my old life": "fresh_start",
            "I was searching for something": "seeking_truth",
            "I don't know yet": "self_discovery"
        },
        "metadata": {
            "location": "hidden_oasis",
            "items": [],
            "npcs": ["old_fisherman"],
            "visited": False
        }
    },

    "ancient_knowledge": {
        "text": (
            "📚 The Wisdom of Ages\n\n"
            "You spend hours studying the ancient symbols, and gradually their "
            "meaning becomes clear. They tell the story of a civilization that "
            "understood the connection between consciousness and reality.\n\n"
            "According to the carvings, this island serves as a bridge between "
            "different states of being. The crystal at its heart is a focusing "
            "device, amplifying the intentions and desires of those who encounter it.\n\n"
            "But there's a warning: 'Those who seek power will find only illusion. "
            "Those who seek wisdom will find transformation. Those who seek nothing "
            "but truth will find everything.'\n\n"
            "The final symbol sequence reveals the location of a hidden chamber "
            "beneath the ruins, where the ancient guardians once underwent their "
            "final transformation.\n\n"
            "Armed with this knowledge, what is your choice?\n"
            "(seek the hidden chamber/return to study the crystal/share this knowledge with others)\n"
        ),
        "choices": {
            "seek the hidden chamber": "guardian_trial",
            "return to study the crystal": "crystal_power",
            "share this knowledge with others": "teacher_path"
        },
        "metadata": {
            "location": "ancient_ruins",
            "items": ["decoded_symbols", "ancient_wisdom"],
            "npcs": [],
            "visited": False
        }
    },

    "watchers_tower": {
        "text": (
            "🗼 The Island's Crown\n\n"
            "The climb to the island's highest point is challenging but rewarding. "
            "At the summit, you find the remains of an ancient stone tower, its "
            "upper floors long since crumbled away.\n\n"
            "But what remains is breathtaking - a circular chamber with windows "
            "facing all directions, offering a complete view of the island and "
            "the endless ocean beyond. In the center sits a stone chair carved "
            "with the same symbols you've seen throughout the island.\n\n"
            "As you sit in the chair, your perspective shifts dramatically. You "
            "can see the island's true nature - not just a physical place, but "
            "a convergence point where different realities meet. You understand "
            "now why so many have been drawn here.\n\n"
            "From this vantage point, you can see several paths leading to different "
            "destinations on the island, each representing a different choice about "
            "your future.\n\n"
            "Which path calls to you?\n"
            "(descend to the crystal chamber/visit the hermit's camp/return to the hidden harbor)\n"
        ),
        "choices": {
            "descend to the crystal chamber": "ancient_ruins",
            "visit the hermit's camp": "smoke_source",
            "return to the hidden harbor": "hidden_harbor"
        },
        "metadata": {
            "location": "watchers_tower",
            "items": ["stone_throne", "tower_ruins"],
            "npcs": [],
            "visited": False
        }
    },

    # Additional ending scenes
    "spiritual_awakening": {
        "text": (
            "🧘 Inner Light\n\n"
            "As you sit in meditation within the crystal circle, you feel your "
            "consciousness expand beyond the boundaries of your physical form. "
            "The crystals resonate with your inner light, creating a harmony "
            "that transcends ordinary experience.\n\n"
            "In this state, you receive visions of the island's true purpose and "
            "your role within the greater cosmic order. You understand that every "
            "choice you've made has led to this moment of awakening.\n\n"
            "When you finally open your eyes, you are fundamentally changed. You "
            "possess an inner peace and clarity that will guide you through any "
            "challenge. Whether you stay on the island or return to the world, "
            "you carry this wisdom with you.\n\n"
            "Years later, people speak of your unusual insight and calming presence. "
            "You help others find their own path to enlightenment, always knowing "
            "that a magical island played a crucial role in your transformation.\n\n"
            "THE END - The Enlightened Path\n\n"
            "🎊 You have achieved the Spiritual Ending! 🎊\n"
            "Through inner reflection, you've found eternal wisdom."
        ),
        "choices": {},
        "metadata": {
            "location": "crystal_chamber",
            "ending_type": "spiritual",
            "items": [],
            "npcs": []
        }
    },

    "promised_return": {
        "text": (
            "🤝 The Keeper of Promises\n\n"
            "You write a solemn promise on a piece of driftwood: 'I will return "
            "to serve as guardian when my time in the outside world is complete.' "
            "As you place it at the shrine, you feel the weight of this commitment "
            "settle into your soul.\n\n"
            "The voyage home is swift and safe, blessed by favorable winds. You "
            "return to your old life, but with a new sense of purpose. You spend "
            "the next decade learning skills that will serve the island well - "
            "medicine, engineering, teaching.\n\n"
            "On your fortieth birthday, you feel the call strongly. You charter "
            "a boat and return to the island, where you find the old fisherman "
            "waiting for you with a knowing smile.\n\n"
            "'Right on time,' he says. 'I've been keeping your promise safe.' "
            "You take up the mantle of guardian, using all you've learned to help "
            "future castaways find their own paths to wisdom.\n\n"
            "THE END - The Promise Keeper\n\n"
            "🎊 You have achieved the Covenant Ending! 🎊\n"
            "Through commitment and preparation, you've found your true calling."
        ),
        "choices": {},
        "metadata": {
            "location": "hidden_harbor",
            "ending_type": "covenant",
            "items": [],
            "npcs": []
        }
    },

    "stormy_departure": {
        "text": (
            "⛈️ The Unworthy Escape\n\n"
            "Ignoring the shrine and the warnings in the logbook, you simply take "
            "the ship and sail away. At first, the winds are favorable, and you "
            "congratulate yourself on your practical approach.\n\n"
            "But as you sail further from the island, the weather begins to turn. "
            "Dark clouds gather, and the wind becomes fierce and chaotic. The "
            "ship, which seemed so seaworthy in the harbor, begins to struggle "
            "against the mounting storm.\n\n"
            "You fight the elements for hours, but eventually, the ship is driven "
            "back toward the island. You crash on the same beach where you first "
            "awakened, the stolen vessel broken beyond repair.\n\n"
            "As you sit in the sand, defeated and humbled, you see a figure "
            "approaching - the old fisherman, carrying supplies and wearing a "
            "compassionate expression.\n\n"
            "'The island has a way of teaching patience,' he says gently. 'Ready "
            "to try again, but with wisdom this time?'\n\n"
            "THE END - The Humbling Return\n\n"
            "🎊 You have achieved the Lesson Ending! 🎊\n"
            "Sometimes we must fail to learn what truly matters."
        ),
        "choices": {},
        "metadata": {
            "location": "shipwreck_beach",
            "ending_type": "lesson",
            "items": [],
            "npcs": ["old_fisherman"]
        }
    },

    # Final missing scenes to complete all paths
    "cave_depths": {
        "text": (
            "🕳️ The Heart of the Island\n\n"
            "The rope bridge creaks ominously but holds your weight as you cross "
            "the underground river. The passage beyond leads even deeper into the "
            "island's core, where you discover a vast chamber filled with ancient "
            "machinery - or what looks like machinery.\n\n"
            "Crystalline formations are integrated with carved stone mechanisms, "
            "creating a fusion of natural and artificial that defies explanation. "
            "The air hums with energy, and you realize you've found the island's "
            "power source.\n\n"
            "At the chamber's center, a throne-like chair faces a massive crystal "
            "formation. This is clearly where the island's guardian would sit to "
            "channel and direct the island's mystical energies.\n\n"
            "As you approach, the crystals begin to resonate with your presence. "
            "You understand that sitting in this chair would grant you incredible "
            "power over the island - but also bind you to it forever.\n\n"
            "What do you choose?\n"
            "(sit in the throne/study the machinery/leave this place)\n"
        ),
        "choices": {
            "sit in the throne": "master_guardian_ending",
            "study the machinery": "ancient_knowledge",
            "leave this place": "cave_left"
        },
        "metadata": {
            "location": "islands_heart",
            "items": ["guardian_throne", "crystal_machinery"],
            "npcs": [],
            "visited": False
        }
    },

    "underwater_treasure": {
        "text": (
            "💎 Sunken Riches\n\n"
            "Wading into the shallow water, you discover a collection of objects "
            "that must have been washed here by the underground current. Among "
            "them are coins, jewelry, and small artifacts from many different "
            "time periods and cultures.\n\n"
            "But the most striking find is a waterproof chest containing a ship's "
            "log and several maps showing safe passage routes around dangerous "
            "waters. These could be incredibly valuable to any sailor.\n\n"
            "As you gather the treasures, you realize this represents the accumulated "
            "wealth of many who have visited the island over the centuries. The "
            "question is: will you use these riches for personal gain, or find "
            "a way to honor their original owners?\n\n"
            "What do you do with this discovery?\n"
            "(take everything for yourself/take only what you need/leave it all for others)\n"
        ),
        "choices": {
            "take everything for yourself": "greedy_ending",
            "take only what you need": "moderate_path",
            "leave it all for others": "selfless_path"
        },
        "metadata": {
            "location": "underground_river",
            "items": ["treasure_chest", "ancient_maps", "accumulated_wealth"],
            "npcs": [],
            "visited": False
        }
    },

    "hidden_cache": {
        "text": (
            "🗝️ The Secret Stash\n\n"
            "Your search reveals a hidden cache buried beneath some rocks near "
            "the shoreline. Inside, you find supplies left by previous visitors: "
            "fresh water, preserved food, tools, and a detailed journal describing "
            "the island's geography and secrets.\n\n"
            "Most importantly, you find a small boat - seaworthy and equipped "
            "with everything needed for ocean travel. A note attached reads: "
            "'For those who choose to leave with wisdom rather than greed. "
            "May fair winds carry you to your destination.'\n\n"
            "This cache represents the island's gift to those who approach it "
            "with respect and humility. You have the means to leave whenever "
            "you choose, but the question remains: what have you learned here "
            "that's worth taking with you?\n\n"
            "What is your decision?\n"
            "(sail away immediately/spend more time learning/help other castaways first)\n"
        ),
        "choices": {
            "sail away immediately": "hasty_departure",
            "spend more time learning": "beach_search",
            "help other castaways first": "helper_path"
        },
        "metadata": {
            "location": "hidden_cache",
            "items": ["seaworthy_boat", "survival_supplies", "island_knowledge"],
            "npcs": [],
            "visited": False
        }
    },

    "survival_wisdom": {
        "text": (
            "🥥 Living with Nature\n\n"
            "Sarah shares her knowledge of island survival with genuine enthusiasm. "
            "She shows you which plants are edible, how to find fresh water, "
            "and techniques for building shelter that work with the island's "
            "unique environment.\n\n"
            "'The key,' she explains, 'is to work with the island, not against it. "
            "Everything here has a purpose, a place in the larger ecosystem. "
            "Once you understand that, survival becomes harmony.'\n\n"
            "She teaches you to read the weather patterns, to understand the "
            "island's moods and rhythms. Under her guidance, you realize that "
            "the island isn't just a place - it's a living entity that responds "
            "to how you treat it.\n\n"
            "Her wisdom extends beyond mere survival to a deeper understanding "
            "of how to live in balance with the natural world.\n\n"
            "What do you want to learn more about?\n"
            "(the island's ecosystem/connecting with nature/finding inner peace)\n"
        ),
        "choices": {
            "the island's ecosystem": "naturalist_path",
            "connecting with nature": "spiritual_connection",
            "finding inner peace": "meditation_ending"
        },
        "metadata": {
            "location": "hermit_camp",
            "items": ["survival_knowledge", "natural_harmony"],
            "npcs": ["sarah_the_hermit"],
            "visited": False
        }
    },

    "island_calling": {
        "text": (
            "🌊 The Heart's True Home\n\n"
            "Sarah smiles wistfully. 'Oh, I tried to leave several times in the "
            "first few years. Built rafts, even found a working radio once. "
            "But every time I was about to go, something would happen - a storm, "
            "a broken mast, or simply a feeling that I wasn't ready yet.'\n\n"
            "'Eventually I realized the island wasn't keeping me prisoner. It was "
            "giving me time to heal, to become who I was meant to be. I'd spent "
            "my whole life studying marine life but never really understanding "
            "my place in the larger web of existence.'\n\n"
            "'Here, I learned that home isn't a place you're born - it's where "
            "you choose to grow. The island called to something in me that had "
            "been sleeping, waiting for the right moment to awaken.'\n\n"
            "She looks at you with understanding eyes. 'The question isn't whether "
            "you can leave, but whether you've found what you came here to find.'\n\n"
            "How do you respond?\n"
            "(I think I understand now/I need more time to decide/I want to explore more)\n"
        ),
        "choices": {
            "I think I understand now": "understanding_ending",
            "I need more time to decide": "contemplation_path",
            "I want to explore more": "smoke_source"
        },
        "metadata": {
            "location": "hermit_camp",
            "items": [],
            "npcs": ["sarah_the_hermit"],
            "visited": False
        }
    },

    "island_truth": {
        "text": (
            "🌟 The Deeper Reality\n\n"
            "Sarah's expression becomes serious and profound. 'This island exists "
            "at the intersection of many realities. It's a place where the veil "
            "between worlds is thin, where consciousness can shape reality more "
            "directly than in the outside world.'\n\n"
            "'The ancient civilization that built the ruins understood this. They "
            "created this place as a school, a testing ground for souls ready "
            "to evolve beyond the limitations of ordinary existence.'\n\n"
            "'Everyone who washes up here is at a crossroads in their spiritual "
            "journey. The island presents them with choices that reveal their "
            "true nature and help them choose their path forward.'\n\n"
            "'Some leave with wisdom and return to transform the world. Others "
            "stay to help guide future seekers. A few discover they're ready "
            "to transcend physical existence entirely.'\n\n"
            "She fixes you with an intense gaze. 'The question is: what kind of "
            "transformation are you ready for?'\n\n"
            "What resonates most deeply with you?\n"
            "(transforming the world/guiding others/transcending physical existence)\n"
        ),
        "choices": {
            "transforming the world": "world_changer_ending",
            "guiding others": "guide_ending",
            "transcending physical existence": "transcendence_ending"
        },
        "metadata": {
            "location": "hermit_camp",
            "items": [],
            "npcs": ["sarah_the_hermit"],
            "visited": False
        }
    },

    "island_teacher_ending": {
        "text": (
            "📚 The Island's Wisdom Keeper\n\n"
            "You decide to remain on the island as a teacher for future castaways. "
            "Working alongside Sarah and the old fisherman, you become part of "
            "a network of guides helping lost souls find their way.\n\n"
            "Over the years, you help dozens of people discover their true path. "
            "Some choose adventure, others find peace, and a few discover powers "
            "they never knew they possessed. Each person you guide teaches you "
            "something new about the infinite possibilities of human potential.\n\n"
            "You develop a deep understanding of the island's mysteries and "
            "become a bridge between the ancient wisdom and modern seekers. "
            "Your presence helps maintain the balance between the mystical "
            "and the practical.\n\n"
            "In your quiet moments, you feel profoundly fulfilled knowing that "
            "you've found your perfect role in the grand tapestry of existence.\n\n"
            "THE END - The Wisdom Keeper\n\n"
            "🎊 You have achieved the Teacher Ending! 🎊\n"
            "Through choosing to guide others, you've found your life's true purpose."
        ),
        "choices": {},
        "metadata": {
            "location": "teaching_grove",
            "ending_type": "teacher",
            "items": [],
            "npcs": []
        }
    },

    "wisdom_sharer_ending": {
        "text": (
            "🌍 The World's Teacher\n\n"
            "You choose to return to the world carrying the island's wisdom. "
            "Your departure is blessed by all the island's guardians, and you "
            "leave with detailed maps, ancient texts, and most importantly, "
            "a deep understanding of how to help others transform their lives.\n\n"
            "Back in civilization, you establish a school that teaches the "
            "principles you learned on the island. Students come from around "
            "the world to learn about consciousness, purpose, and the hidden "
            "potentials that lie within every human being.\n\n"
            "Your teachings spread gradually but powerfully, creating a network "
            "of wise teachers who carry the island's influence to every corner "
            "of the globe. Some of your students even find their way to the "
            "island itself, continuing the cycle of wisdom.\n\n"
            "Years later, you look back with satisfaction at the countless lives "
            "you've helped transform through the gifts the island gave you.\n\n"
            "THE END - The Global Teacher\n\n"
            "🎊 You have achieved the World Changer Ending! 🎊\n"
            "Through sharing wisdom globally, you've multiplied the island's influence infinitely."
        ),
        "choices": {},
        "metadata": {
            "location": "wisdom_school",
            "ending_type": "world_changer",
            "items": [],
            "npcs": []
        }
    },

    "world_changer_ending": {
        "text": (
            "🌎 The Revolutionary\n\n"
            "Inspired by Sarah's words about transforming the world, you choose "
            "to leave the island with a mission to revolutionize how humanity "
            "understands consciousness and reality.\n\n"
            "You become a pioneer in bridging science and spirituality, using "
            "your island experiences to inspire breakthrough research in quantum "
            "physics, consciousness studies, and human potential.\n\n"
            "Through books, lectures, and direct action, you help shift humanity's "
            "worldview toward a more connected, compassionate understanding of "
            "existence. Your work contributes to solving global challenges by "
            "helping people see beyond their limited perspectives.\n\n"
            "The island's influence spreads through your work, touching millions "
            "of lives and helping to create a more enlightened world.\n\n"
            "THE END - The World Transformer\n\n"
            "🎊 You have achieved the Revolutionary Ending! 🎊\n"
            "Through bold action, you've helped evolve human consciousness on a global scale."
        ),
        "choices": {},
        "metadata": {
            "location": "global_stage",
            "ending_type": "revolutionary",
            "items": [],
            "npcs": []
        }
    },

    "guide_ending": {
        "text": (
            "🧭 The Eternal Guide\n\n"
            "You choose to dedicate your life to guiding others, but not necessarily "
            "by staying on the island. Instead, you become a wandering teacher, "
            "appearing in the lives of those who need guidance most.\n\n"
            "Sometimes you help shipwreck survivors find safety. Other times you "
            "appear to people facing life crises, offering exactly the wisdom "
            "they need to move forward. You've become a bridge between the "
            "mystical island and the everyday world.\n\n"
            "Your life becomes a series of meaningful encounters, each one an "
            "opportunity to share the island's gifts with someone ready to receive "
            "them. You find deep fulfillment in this role as a catalyst for "
            "others' transformations.\n\n"
            "Though you age, your spirit remains timeless, carrying the island's "
            "eternal wisdom wherever guidance is needed most.\n\n"
            "THE END - The Wandering Guide\n\n"
            "🎊 You have achieved the Eternal Guide Ending! 🎊\n"
            "Through dedicating your life to guidance, you've become a living bridge of wisdom."
        ),
        "choices": {},
        "metadata": {
            "location": "wandering_path",
            "ending_type": "eternal_guide",
            "items": [],
            "npcs": []
        }
    }
}