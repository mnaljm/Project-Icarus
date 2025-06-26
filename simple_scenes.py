# SIMPLIFIED TEST STORY FOR PROJECT ICARUS
# A complete, functional story with multiple paths and endings

scenes = {
    "opening": {
        "text": (
            "🏝️ Welcome to Mystery Island\n\n"
            "You wake up on a sandy beach after your boat was destroyed in a storm. "
            "The sun is setting, and you need to find shelter for the night.\n\n"
            "Looking around, you see three options:\n"
            "- A cave in the rocky cliffs to your right\n"
            "- Dense jungle straight ahead\n"
            "- The remains of an old campfire to your left\n\n"
            "Where do you go first?\n"
            "(explore cave/enter jungle/investigate campfire)\n"
        ),
        "choices": {
            "explore cave": "cave_discovery",
            "enter jungle": "jungle_path",
            "investigate campfire": "old_camp"
        },
        "metadata": {
            "location": "beach",
            "items": [],
            "npcs": [],
            "visited": False
        }
    },

    "cave_discovery": {
        "text": (
            "🕳️ The Hidden Cave\n\n"
            "The cave is dry and spacious. Ancient drawings cover the walls, "
            "depicting people arriving by boat and finding some kind of treasure.\n\n"
            "In the back of the cave, you find a chest containing:\n"
            "- A detailed map of the island\n"
            "- An old journal with notes about hidden treasures\n"
            "- A rusty but functional compass\n\n"
            "The journal mentions three important locations: the Wisdom Tree "
            "in the jungle center, the Golden Beach on the far shore, and the "
            "Temple of Choices at the island's peak.\n\n"
            "Which location interests you most?\n"
            "(seek wisdom tree/find golden beach/climb to temple)\n"
        ),
        "choices": {
            "seek wisdom tree": "wisdom_tree",
            "find golden beach": "golden_beach",
            "climb to temple": "choice_temple"
        },
        "metadata": {
            "location": "ancient_cave",
            "items": ["island_map", "treasure_journal", "compass"],
            "npcs": [],
            "visited": False
        }
    },

    "jungle_path": {
        "text": (
            "🌿 Into the Green\n\n"
            "The jungle is thick but passable. You follow what seems to be an "
            "old trail. After an hour of walking, you encounter a friendly old "
            "man sitting by a small stream.\n\n"
            "'Ah, another castaway!' he says with a warm smile. 'I'm Marcus. "
            "Been living on this island for five years now. It's actually quite "
            "wonderful once you learn its secrets.'\n\n"
            "He offers to teach you about the island. 'There are three paths "
            "a person can take here,' he explains. 'The path of knowledge, "
            "the path of wealth, or the path of service to others.'\n\n"
            "Which path appeals to you?\n"
            "(choose knowledge/choose wealth/choose service)\n"
        ),
        "choices": {
            "choose knowledge": "knowledge_path",
            "choose wealth": "wealth_path",
            "choose service": "service_path"
        },
        "metadata": {
            "location": "jungle_stream",
            "items": ["fresh_water"],
            "npcs": ["marcus_the_guide"],
            "visited": False
        }
    },

    "old_camp": {
        "text": (
            "🔥 The Previous Visitor\n\n"
            "The campfire is cold but recently used. Searching around, you find "
            "supplies: canned food, fresh water, and a note that reads:\n\n"
            "'To whoever finds this - I've gone to explore the island's three "
            "legendary sites. If I don't return in a week, use these supplies "
            "to build a raft and escape. The island is beautiful but dangerous "
            "for those who aren't ready for its tests. - Elena'\n\n"
            "You also find a rough map showing three marked locations and several "
            "possible paths to each one.\n\n"
            "What do you decide to do?\n"
            "(follow Elena's trail/explore on your own/build the escape raft)\n"
        ),
        "choices": {
            "follow Elena's trail": "search_for_elena",
            "explore on your own": "solo_exploration",
            "build the escape raft": "quick_escape"
        },
        "metadata": {
            "location": "abandoned_camp",
            "items": ["survival_supplies", "elenas_map", "raft_materials"],
            "npcs": [],
            "visited": False
        }
    },

    # Knowledge Path Endings
    "wisdom_tree": {
        "text": (
            "🌳 The Ancient Wisdom\n\n"
            "You find the massive tree at the island's center. Its trunk is "
            "covered with carvings in an ancient language that somehow you can "
            "understand. The tree speaks to your mind:\n\n"
            "'Seeker of wisdom, you have found the source of understanding. "
            "I offer you knowledge of the cosmos, the secrets of life and death, "
            "and the power to help others find their true path.'\n\n"
            "As you touch the tree, profound knowledge flows into your mind. "
            "You understand your purpose now - to return to the world as a "
            "teacher and guide for others seeking meaning.\n\n"
            "THE END - The Wise Teacher\n\n"
            "🎊 You have achieved the Wisdom Ending! 🎊\n"
            "Through seeking knowledge, you've found your calling as a guide for others."
        ),
        "choices": {},
        "metadata": {
            "location": "wisdom_tree",
            "ending_type": "wisdom",
            "items": [],
            "npcs": []
        }
    },

    "knowledge_path": {
        "text": (
            "📚 The Scholar's Journey\n\n"
            "Marcus leads you to a hidden library built into a massive tree. "
            "The books here contain knowledge from civilizations across the "
            "world and throughout history.\n\n"
            "'This is the Island's greatest treasure,' Marcus explains. 'Knowledge "
            "that can help humanity solve its greatest challenges. But it comes "
            "with responsibility - you must use it wisely.'\n\n"
            "You spend weeks studying, learning about medicine, technology, "
            "philosophy, and the deeper mysteries of existence. When you're "
            "ready to leave, you carry with you solutions to problems that "
            "have plagued humanity for centuries.\n\n"
            "THE END - The Knowledge Bearer\n\n"
            "🎊 You have achieved the Scholar Ending! 🎊\n"
            "Through dedication to learning, you've become humanity's teacher."
        ),
        "choices": {},
        "metadata": {
            "location": "tree_library",
            "ending_type": "scholar",
            "items": [],
            "npcs": ["marcus_the_guide"]
        }
    },

    # Wealth Path Endings
    "golden_beach": {
        "text": (
            "🏖️ The Treasure Shore\n\n"
            "Following the map, you discover a beach where the sand glitters "
            "with gold dust. Scattered across the shore are chests of treasure "
            "from shipwrecks spanning centuries.\n\n"
            "But as you begin collecting the wealth, you notice something strange. "
            "The more you take, the heavier your heart becomes. The gold feels "
            "cold and lifeless in your hands.\n\n"
            "A voice whispers on the wind: 'True treasure cannot be hoarded. "
            "It must be shared to have meaning.'\n\n"
            "You realize that taking this wealth for yourself would make you "
            "rich but empty. Instead, you decide to use it to help others.\n\n"
            "THE END - The Generous Heart\n\n"
            "🎊 You have achieved the Generosity Ending! 🎊\n"
            "Through choosing to share rather than hoard, you've found true wealth."
        ),
        "choices": {},
        "metadata": {
            "location": "golden_beach",
            "ending_type": "generosity",
            "items": [],
            "npcs": []
        }
    },

    "wealth_path": {
        "text": (
            "💰 The Treasure Hunter's Dream\n\n"
            "Marcus reluctantly leads you to a hidden valley filled with "
            "precious gems and gold. 'Many have chosen this path,' he sighs. "
            "'Few find happiness in it.'\n\n"
            "You could take enough treasure to live luxuriously forever. But "
            "as you fill your pockets, you notice Marcus's sad expression.\n\n"
            "'The island gives each person what they think they want,' he says. "
            "'But it also shows them what they truly need. The choice is yours - "
            "material wealth or spiritual richness.'\n\n"
            "You pause, looking at the gold in your hands, then at Marcus's "
            "peaceful, content face. You realize true wealth might be something "
            "entirely different.\n\n"
            "THE END - The Enlightened Choice\n\n"
            "🎊 You have achieved the Realization Ending! 🎊\n"
            "Through temptation, you've discovered what truly matters."
        ),
        "choices": {},
        "metadata": {
            "location": "treasure_valley",
            "ending_type": "realization",
            "items": [],
            "npcs": ["marcus_the_guide"]
        }
    },

    # Service Path Endings
    "choice_temple": {
        "text": (
            "⛩️ The Temple of Decisions\n\n"
            "At the island's peak stands an ancient temple. Inside, three "
            "doors await, each marked with a symbol: a book, a coin, and "
            "a helping hand.\n\n"
            "A serene voice fills the temple: 'Choose the path that represents "
            "your heart's true desire. Each leads to a different destiny, "
            "each valuable in its own way.'\n\n"
            "You understand that this is the island's final test - not of "
            "your abilities, but of your character and deepest values.\n\n"
            "Which door calls to your soul?\n"
            "(door of knowledge/door of wealth/door of service)\n"
        ),
        "choices": {
            "door of knowledge": "temple_wisdom",
            "door of wealth": "temple_treasure",
            "door of service": "temple_service"
        },
        "metadata": {
            "location": "choice_temple",
            "items": [],
            "npcs": [],
            "visited": False
        }
    },

    "service_path": {
        "text": (
            "🤝 The Helper's Reward\n\n"
            "Marcus beams with joy. 'The path of service - the rarest and "
            "most beautiful choice!' He leads you to a gathering of all the "
            "island's inhabitants - other castaways who chose to stay and "
            "help future visitors.\n\n"
            "'Welcome to our community,' they say. 'We are the island's "
            "guardians, helping lost souls find their way, just as someone "
            "once helped us.'\n\n"
            "You spend your days building shelters, leaving supplies for "
            "castaways, and offering guidance to those who need it. You "
            "find deep fulfillment in this life of service.\n\n"
            "Years later, you realize you've found something more valuable "
            "than gold or knowledge - a life of purpose and meaning.\n\n"
            "THE END - The Guardian's Peace\n\n"
            "🎊 You have achieved the Service Ending! 🎊\n"
            "Through serving others, you've found your true home and purpose."
        ),
        "choices": {},
        "metadata": {
            "location": "guardian_community",
            "ending_type": "service",
            "items": [],
            "npcs": ["marcus_the_guide", "island_community"]
        }
    },

    # Search for Elena Endings
    "search_for_elena": {
        "text": (
            "🔍 Following the Trail\n\n"
            "You follow Elena's path marked on the map. After a day of searching, "
            "you find her at the Wisdom Tree, deep in meditation.\n\n"
            "'I was wondering when someone would follow my trail,' she says "
            "with a smile. 'I've been learning from the island's spirit. "
            "It's shown me that everyone who arrives here is meant to discover "
            "something about themselves.'\n\n"
            "'I've decided to stay and become one of the island's guides. "
            "But you have your own choice to make. What does your heart tell "
            "you about why you're here?'\n\n"
            "Her question resonates deeply. You realize this isn't about "
            "rescuing her - it's about discovering your own path.\n\n"
            "THE END - The Self-Discovery\n\n"
            "🎊 You have achieved the Discovery Ending! 🎊\n"
            "Through helping others, you've found your own purpose."
        ),
        "choices": {},
        "metadata": {
            "location": "wisdom_tree",
            "ending_type": "discovery",
            "items": [],
            "npcs": ["elena_the_seeker"]
        }
    },

    # Solo Exploration Endings
    "solo_exploration": {
        "text": (
            "🗺️ The Independent Path\n\n"
            "You decide to explore the island on your own terms, without "
            "following anyone else's path. This journey of independence leads "
            "you to discover hidden wonders that no map has marked.\n\n"
            "You find secret waterfalls, caves filled with crystals, and "
            "viewpoints that show the island's breathtaking beauty. Most "
            "importantly, you discover your own inner strength and resourcefulness.\n\n"
            "When you eventually choose to leave the island, you do so with "
            "complete confidence in your ability to face any challenge. The "
            "island has taught you that sometimes the best path is the one "
            "you create yourself.\n\n"
            "THE END - The Self-Reliant Explorer\n\n"
            "🎊 You have achieved the Independence Ending! 🎊\n"
            "Through trusting yourself, you've gained unshakeable confidence."
        ),
        "choices": {},
        "metadata": {
            "location": "unexplored_territories",
            "ending_type": "independence",
            "items": [],
            "npcs": []
        }
    },

    # Quick Escape Ending
    "quick_escape": {
        "text": (
            "🛶 The Cautious Departure\n\n"
            "Using Elena's supplies and following her notes, you successfully "
            "build a raft and sail away from the island. Your practical approach "
            "gets you safely back to civilization.\n\n"
            "However, as you return to your normal life, you find yourself "
            "constantly thinking about the island and wondering what adventures "
            "you might have experienced if you'd been braver.\n\n"
            "Still, you're proud of your survival instincts and practical "
            "thinking. Not every adventure needs to be taken - sometimes "
            "wisdom lies in knowing when to leave.\n\n"
            "You return to your life with a new appreciation for both adventure "
            "and the comfort of home.\n\n"
            "THE END - The Practical Escape\n\n"
            "🎊 You have achieved the Survivor Ending! 🎊\n"
            "Through practical thinking, you've safely returned home with valuable perspective."
        ),
        "choices": {},
        "metadata": {
            "location": "open_ocean",
            "ending_type": "survivor",
            "items": [],
            "npcs": []
        }
    },

    # Additional Temple Endings
    "temple_wisdom": {
        "text": (
            "📖 The Door of Knowledge\n\n"
            "Choosing the door marked with a book, you enter a chamber filled "
            "with floating scrolls and glowing texts. Ancient wisdom from "
            "every civilization flows into your mind.\n\n"
            "You emerge from the temple as a keeper of universal knowledge, "
            "understanding the deepest mysteries of existence. This gift comes "
            "with the responsibility to teach and guide others.\n\n"
            "THE END - The Universal Scholar\n\n"
            "🎊 You have achieved the Ultimate Wisdom Ending! 🎊\n"
            "Through the temple's test, you've become a master of all knowledge."
        ),
        "choices": {},
        "metadata": {
            "location": "temple_of_knowledge",
            "ending_type": "universal_wisdom",
            "items": [],
            "npcs": []
        }
    },

    "temple_treasure": {
        "text": (
            "💎 The Door of Wealth\n\n"
            "Behind the coin-marked door lies not gold, but something far more "
            "valuable - the understanding of true abundance. You learn that "
            "real wealth comes from having enough to share.\n\n"
            "The temple grants you the ability to always find what you need "
            "and the wisdom to know the difference between wants and needs.\n\n"
            "THE END - The Abundant Life\n\n"
            "🎊 You have achieved the True Wealth Ending! 🎊\n"
            "Through the temple's lesson, you've learned the secret of real abundance."
        ),
        "choices": {},
        "metadata": {
            "location": "temple_of_abundance",
            "ending_type": "true_wealth",
            "items": [],
            "npcs": []
        }
    },

    "temple_service": {
        "text": (
            "🙏 The Door of Service\n\n"
            "The door marked with a helping hand leads to a chamber where you "
            "experience the joy and fulfillment of everyone you could ever help. "
            "You understand that service to others is the highest calling.\n\n"
            "The temple blesses you with the ability to always know how to help "
            "others and the strength to do so selflessly.\n\n"
            "THE END - The Blessed Servant\n\n"
            "🎊 You have achieved the Divine Service Ending! 🎊\n"
            "Through choosing service, you've received the greatest blessing of all."
        ),
        "choices": {},
        "metadata": {
            "location": "temple_of_service",
            "ending_type": "divine_service",
            "items": [],
            "npcs": []
        }
    }
}
