# Project Icarus 🚀

A text-based adventure game built in Python as a final project for basic Python programming.

## 📖 Overview

Project Icarus is an interactive text adventure game where players navigate through various scenes, make choices that affect the story outcome, and manage an inventory system with items that have unique stats and properties.

## 🎮 Features

- **Interactive Storytelling**: Navigate through multiple scenes with branching narratives
- **Choice-Based Gameplay**: Your decisions determine the story path and outcomes
- **Item Stats**: Items have unique properties like damage, healing, durability, and special abilities
- **Metadata Tracking**: Scenes track visited locations, available items, and NPCs
- **Clean Console Interface**: Clear screen functionality for better user experience

## 🚀 How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. **Basic Commands**:
   - Type your choice when prompted (e.g., "wall", "glint")
   - `exit` - Quit the game
   - `inventory` - View your current items
   - `inspect [item]` - View detailed item information and stats
   - `use [item]` - Use an item from your inventory
   - `stats` - View your current player stats
   - `take [item]` - Pick up items from the environment

3. **Gameplay Tips**:
   - Read scene descriptions carefully for clues
   - Some items can be used multiple times, others are consumable
   - Track your health and light levels
   - Explore all available choices for different story outcomes


## 🛠️ Technical Features

- **Modular Design**: Scenes and items are separated for easy content management
- **Extensible Framework**: Easy to add new scenes, items, and game mechanics
- **Error Handling**: Graceful handling of invalid inputs and edge cases
- **Cross-Platform**: Compatible with Windows, macOS, and Linux

## 🎯 Game Mechanics

### Scene System
- Each scene contains descriptive text and available choices
- Metadata tracks location, items, NPCs, and visit status
- Branching narrative with multiple possible outcomes

## 🔧 Customization

The game is designed to be easily customizable:

1. **Add New Scenes**: Edit `scenes.py` to add new story content
2. **Modify Game Logic**: Update `main.py` to add new game mechanics

## 📝 Development Notes

This project demonstrates:
- Python fundamentals (variables, functions, loops, conditionals)
- Data structures (dictionaries, lists)
- File organization and modular programming
- User input handling and validation
- String manipulation and formatting

## 🎓 Learning Objectives

- Practice Python syntax and core concepts
- Implement game logic and state management
- Work with nested data structures
- Handle user input and error cases
- Create an interactive console application

---

*Built with ❤️ using Python for final week programming project*