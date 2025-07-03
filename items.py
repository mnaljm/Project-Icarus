# ITEM DATA TEMPLATE
# This file contains all the items for the text adventure game
# Each item has a name, description, and metadata

# ITEM STRUCTURE TEMPLATE:
# "item_name": {
#     "description": "A brief description of the item.",
#     "metadata": { 
#         "type": "weapon",  # e.g., "weapon", "potion", "key",
#         "value": 10,  # e.g., value for trading or effects,
#         "effects": ["healing", "damage"],  # e.g., effects the item has,
#         "base_stats": {  # e.g., base stats for weapons,
#             "damage": 5,
#             "defense": 0,
#             "healing": 0
#         },
#     }
# }

items = {
    # WEAPONS
    "rusty_sword": {
        "description": "An old, weathered sword with rust spots along the blade. +5 damage.",
        "metadata": { 
            "type": "weapon",
            "value": 10,
            "effects": ["damage"],
            "base_stats": {
                "damage": 5,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "dagger": {
        "description": "A sharp dagger with a leather-wrapped handle. +3 damage.",
        "metadata": {
            "type": "weapon",
            "value": 15,
            "effects": ["damage"],
            "base_stats": {
                "damage": 3,
                "defense": 0,
                "healing": 0
            },
        }
    },
    
    # TOOLS
    "rusty_lockpick": {
        "description": "A rusty lockpick, barely functional but still usable.",
        "metadata": {
            "type": "tool",
            "value": 5,
            "effects": ["unlock"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    
    # POTIONS
    "sleep_draught": {
        "description": "A potion that induces sleep, useful for stealth.",
        "metadata": {
            "type": "potion",
            "value": 20,
            "effects": ["sleep"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    
    # Quest ITEMS
    "temple_note": {
        "description": "A note found in the storeroom of the prison. 'The elder is awaiting your reply'.",
        "metadata": {
            "type": "note",
            "value": 0,
            "effects": ["quest"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "temple_map": {
        "description": "A worn map with markings leading to a 'Sunken Temple'.",
        "metadata": {
            "type": "map",
            "value": 0,
            "effects": ["quest"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "stone_pendant": {
        "description": "A strange stone pendant, possibly of some significance.",
        "metadata": {
            "type": "artifact",
            "value": 0,
            "effects": ["quest"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "relic_of_the_gods": {
        "description": "An ancient relic said to hold immense power.",
        "metadata": {
            "type": "relic",
            "value": 100,
            "effects": ["power"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    # MISC ITEMS
    "ancient_knowledge": { 
        "description": "A fragment of ancient knowledge, glowing faintly.",
        "metadata": {
            "type": "knowledge",
            "value": 50,
            "effects": ["wisdom"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "ancient_scroll": {
        "description": "An ancient scroll with cryptic symbols, possibly a spell.",
        "metadata": {
            "type": "scroll",
            "value": 30,
            "effects": ["magic"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "temple_directions": {
        "description": "A set of directions leading to the Sunken Temple.",
        "metadata": {
            "type": "directions",
            "value": 0,
            "effects": ["navigation"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "priests_blessing": {
        "description": "A blessing from the temple priest, granting protection.",
        "metadata": {
            "type": "blessing",
            "value": 0,
            "effects": ["protection"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "travel_supplies": {
        "description": "A bundle of supplies for long journeys, including food and water.",
        "metadata": {
            "type": "supplies",
            "value": 25,
            "effects": ["sustenance"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 10,
            },
        },
    },
    "local_map": {
        "description": "A map of the local area, useful for navigation.",
        "metadata": {
            "type": "map",
            "value": 0,
            "effects": ["navigation"],
            "base_stats": {
                "damage": 0,
                "defense": 0,
                "healing": 0
            },
        },
    },
    "sturdy_knife": {
        "description": "A sturdy knife, useful for cutting and carving. +9 damage.",
        "metadata": {
            "type": "tool",
            "value": 10,
            "effects": ["cutting"],
            "base_stats": {
                "damage": 9,
                "defense": 0,
                "healing": 0
            },
        }
    },
    "leather_vest": {
        "description": "A simple leather vest, providing basic protection. +2 defense.",
        "metadata": {
            "type": "armor",
            "value": 15,
            "effects": ["defense"],
            "base_stats": {
                "damage": 0,
                "defense": 2,
                "healing": 0
            },
        },
    },
}