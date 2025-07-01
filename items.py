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
    "rusty_sword": {
        "description": "An old, weathered sword with rust spots along the blade.",
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
    }
}