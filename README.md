# Project Icarus 🚀

A comprehensive text-based adventure game built in Python featuring prison escape, exploration, combat, and multiple branching storylines with speedrun capabilities.

## 📖 Story Overview

You wake up in a cold, damp prison cell with your hands free from shackles. Navigate through a rich fantasy world where your choices determine your fate. Escape from prison, explore a mysterious town, uncover ancient temple secrets, and face off against cultists in pursuit of the legendary Relic of the Gods.

**Featuring 6 chapters:**
- **Chapter 1**: Prison Escape (Stealth or Combat paths)
- **Chapter 2**: The Outside World (Forest exploration)
- **Chapter 3**: Town Sequence (Gathering intel and supplies)
- **Chapter 4**: Temple Approach (Multiple discovery routes)
- **Chapter 5**: Inside the Temple (Cultist encounters and puzzles)
- **Chapter 6**: Multiple Endings (7 different endings based on your choices)

## 🎮 Core Features

### 🎭 **Rich Storytelling System**
- **50+ unique scenes** with atmospheric descriptions
- **Branching narrative** with meaningful choice consequences
- **Multiple story paths**: Stealth vs Combat approaches
- **7 different endings** including Divine Ascension, Relic Master, and Survivor's Escape

### ⚔️ **Combat System**
- Turn-based combat with hit/miss mechanics
- **Weapon damage bonuses** from inventory items
- **Enemy variety**: Training dummies, guards, bandits, and cultists
- Health management with death/restart mechanics

### 🎒 **Inventory & Items System**
- **15+ collectible items** including weapons, tools, and quest items
- **Item categories**: Weapons, Tools, Potions, Quest Items, and Artifacts
- **Smart item pickup**: "take [item]" and "pick up [item]" commands
- **Item effects**: Damage bonuses, unlock abilities, quest progression

### 🎲 **Skill Check System**
- **D20 dice rolling** with visual rolling animation
- **Three difficulty levels**: Easy (5+), Medium (10+), Hard (15+)
- **Dynamic choice removal** on failed attempts
- **Atmospheric tension** with suspenseful dice rolling

### ⏱️ **Speedrun Mode**
- **Real-time speedrun timer** displayed during gameplay
- **Personal best tracking** for current session
- **Leaderboard system** with formatted MM:SS.ss times
- **Completion time display** at game end

### 🎯 **Advanced Game Mechanics**
- **Choice requirement system**: Items unlock new options
- **Smart input matching**: Partial text recognition and autocomplete
- **Scene metadata**: Items, clues, and skill checks per location
- **Cross-platform compatibility**: Windows, macOS, and Linux

## 🚀 How to Play

1. **Start the game:**
   ```bash
   python main.py
   ```

2. **Navigation:**
   - Choose from available options by typing your selection
   - Use partial matching to navigate scenes
   - Type "inventory" or "i" to check your items

3. **Combat:**
   - Type "attack" to engage enemies
   - Your total damage = base damage + weapon bonuses
   - Manage your health carefully - death sends you back to main menu

4. **Item Interaction:**
   - Use "take [item]" or "pick up [item]" to collect items
   - Some items unlock new dialogue options or abilities
   - Weapons automatically add damage bonuses

5. **Speedrunning:**
   - Select "Start Game" for timed gameplay
   - Your time is displayed continuously during play
   - Aim for different endings to find the fastest route

6. **Replayability:**
   - Inventory persists across games to allow new routes based on items not available first time
   - Select "Start New Run" to wipe your inventory if you want to start over entirely
   - Multiple story paths: Stealth vs Combat routes offer completely different experiences
   - Failed skill checks remove choices permanently, encouraging different approaches on replay


## 🎯 Game Systems

### Scene Structure
```python
"scene_name": {
    "text": "Scene description...",
    "choices": {"choice1": "next_scene"},
    "metadata": {
        "items": ["item_list"],
        "skill_check": {"choice": "difficulty"},
    }
}
```

### Item System
- **Weapons**: Rusty Sword (+5 damage), Dagger (+3 damage)
- **Tools**: Lockpick (unlock doors), Sleep Draught (stealth)
- **Quest Items**: Temple Map, Stone Pendant, Ancient Knowledge
- **Artifacts**: Relic of the Gods (ultimate prize)

### Combat Mechanics
- **Hit Chance**: Random roll vs enemy dodge rating
- **Damage Calculation**: Base damage + weapon bonuses
- **Enemy Types**: Various HP pools and damage ratings
- **Victory Conditions**: Reduce enemy HP to 0

## 🗂️ Project Structure

```
Project-Icarus/
├── main.py                           # Core game engine and main loop
├── scenes.py                         # All story content and scene data
├── items.py                          # Item definitions and metadata
├── Random dice roll advantage.py     # Dice utility functions
├── Random dice roll disadvantage.py  # Additional dice mechanics
└── README.md                         # This file
```

## 🔧 Technical Implementation

### Core Technologies
- **Pure Python 3**: No external dependencies required
- **Modular Architecture**: Separated concerns across multiple files
- **Object-oriented Design**: Player stats, items, and scene management
- **Error Handling**: Graceful invalid input management

### Key Features
- **Smart Input Processing**: Fuzzy matching with user feedback
- **State Management**: Player stats, inventory, and scene progression
- **Dynamic Content**: Items disappear after pickup, choices change based on items
- **Visual Feedback**: Color-coded messages for success/failure/info
- **Time Management**: Built-in delays for dramatic effect

## 🎓 Educational Value

This project demonstrates mastery of:
- **Python Fundamentals**: Variables, functions, loops, conditionals
- **Data Structures**: Complex nested dictionaries and lists
- **File Organization**: Multi-file project structure
- **Game Logic**: State machines, combat systems, progression tracking
- **User Experience**: Input validation, clear feedback, error handling
- **Advanced Features**: Timing systems, dynamic content, requirements checking

## Endings Guide

**Multiple paths lead to different endings:**
1. **Sacrificial Death** - Ultimate sacrifice at the altar
2. **Divine Ascension** - Become a vessel for the gods
3. **Relic Master** - Claim the relic through combat or wisdom
4. **Divine Ruler** - Return to town with divine power
5. **Survivor's Escape** - Escape without the relic but alive

---

*A complete text adventure experience showcasing advanced Python programming concepts and game design principles.*