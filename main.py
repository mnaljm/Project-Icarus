# PROJECT ICARUS - MAIN GAME ENGINE
# Text-based adventure game with scene management system

# IMPORTS
import os
import json
import time
from datetime import datetime
from pathlib import Path
from scenes import scenes

# GAME CONFIGURATION
GAME_TITLE = "Project Icarus"
GAME_VERSION = "0.1.0"

# Create saves directory in user's home directory to avoid permission issues
SAVES_DIR = Path.home() / "Documents" / "ProjectIcarus" / "saves"
SAVES_DIR.mkdir(parents=True, exist_ok=True)
SAVE_FILE = SAVES_DIR / "savegame.json"

# GAME STATE VARIABLES
class GameState:
    def __init__(self):
        self.player_choices = []  # Track all player choices
        self.current_scene = "opening"  # Starting scene
        self.visited_scenes = set()  # Track visited scenes
        self.game_stats = {
            "start_time": datetime.now().isoformat(),
            "scenes_visited": 0,
            "choices_made": 0,
            "current_playthrough": 1
        }
        self.player_inventory = []  # For future item system
        self.player_name = "Player"  # Default name

# Initialize game state
game_state = GameState()

# UTILITY FUNCTIONS
def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_separator(char="-", length=60):
    """Print a separator line."""
    print(char * length)

def print_title():
    """Print the game title and version."""
    clear_screen()
    print("=" * 60)
    print(f"  {GAME_TITLE.upper()} - v{GAME_VERSION}")
    print("  Text Adventure Game")
    print("=" * 60)
    print()

def print_game_stats():
    """Print current game statistics."""
    print(f"📊 Game Stats:")
    print(f"   Scenes Visited: {game_state.game_stats['scenes_visited']}")
    print(f"   Choices Made: {game_state.game_stats['choices_made']}")
    if game_state.player_choices:
        print(f"   Recent Choices: {' → '.join(game_state.player_choices[-3:])}")
    print()

def wait_for_input(prompt="Press Enter to continue..."):
    """Wait for user input with custom prompt."""
    print(prompt)
    input()

# SAVE/LOAD SYSTEM
def save_game():
    """Save the current game state to file."""
    try:
        save_data = {
            "player_choices": game_state.player_choices,
            "current_scene": game_state.current_scene,
            "visited_scenes": list(game_state.visited_scenes),
            "game_stats": game_state.game_stats,
            "player_inventory": game_state.player_inventory,
            "player_name": game_state.player_name,
            "save_time": datetime.now().isoformat()
        }
        
        with open(SAVE_FILE, 'w') as f:
            json.dump(save_data, f, indent=2)
        
        print(f"✅ Game saved successfully!")
        print(f"   Save location: {SAVE_FILE}")
        return True
    except Exception as e:
        print(f"❌ Failed to save game: {e}")
        print(f"   Attempted save location: {SAVE_FILE}")
        return False

def load_game():
    """Load game state from file."""
    try:
        if not SAVE_FILE.exists():
            print("❌ No save file found.")
            print(f"   Looking for save at: {SAVE_FILE}")
            return False
            
        with open(SAVE_FILE, 'r') as f:
            save_data = json.load(f)
        
        # Restore game state
        game_state.player_choices = save_data.get("player_choices", [])
        game_state.current_scene = save_data.get("current_scene", "opening")
        game_state.visited_scenes = set(save_data.get("visited_scenes", []))
        game_state.game_stats = save_data.get("game_stats", game_state.game_stats)
        game_state.player_inventory = save_data.get("player_inventory", [])
        game_state.player_name = save_data.get("player_name", "Player")
        
        print(f"✅ Game loaded successfully!")
        print(f"   Last saved: {save_data.get('save_time', 'Unknown')}")
        return True
    except Exception as e:
        print(f"❌ Failed to load game: {e}")
        return False

# INPUT HANDLING
def get_user_choice(prompt, valid_choices):
    """Get user input and validate it against a list of valid choices."""
    while True:
        print(f"\n{prompt}")
        user_input = input("> ").lower().strip()
        
        # Check for special commands
        if user_input in ['save', 'load', 'quit', 'help', 'stats']:
            return user_input
        
        # Check if the input matches any of the valid choices
        for choice in valid_choices:
            if user_input == choice.lower() or user_input in choice.lower():
                return choice
        
        print(f"❌ Invalid choice. Please choose from: {', '.join(valid_choices)}")
        print("💡 Special commands: save, load, quit, help, stats")

def handle_special_command(command):
    """Handle special game commands."""
    if command == "save":
        save_game()
        wait_for_input()
        return False
    elif command == "load":
        if load_game():
            print("Game state restored!")
        wait_for_input()
        return False
    elif command == "quit":
        print("Thanks for playing Project Icarus!")
        return True
    elif command == "help":
        show_help()
        wait_for_input()
        return False
    elif command == "stats":
        print_game_stats()
        wait_for_input()
        return False
    return False

def show_help():
    """Display help information."""
    print("\n📖 HELP - Available Commands:")
    print("   • Type your choice (or part of it) to select an option")
    print("   • 'save' - Save your current progress")
    print("   • 'load' - Load a previously saved game")
    print("   • 'stats' - View your game statistics")
    print("   • 'help' - Show this help message")
    print("   • 'quit' - Exit the game")
    print("\n💡 Tips:")
    print("   • You can type partial matches (e.g., 'look' for 'look through the crack')")
    print("   • Your choices are saved automatically when you save the game")
    print("   • Some scenes may have hidden elements to discover!")
    print(f"\n💾 Save Information:")
    print(f"   • Save files are stored in: {SAVES_DIR}")
    print(f"   • This location avoids permission issues")
    print(f"   • Your progress is safe and persistent")

# SCENE MANAGEMENT
def display_scene(scene_name):
    """Display a scene and handle user interaction."""
    if scene_name not in scenes:
        print(f"❌ Error: Scene '{scene_name}' not found!")
        return None
    
    scene = scenes[scene_name]
    
    # Mark scene as visited
    if scene_name not in game_state.visited_scenes:
        game_state.visited_scenes.add(scene_name)
        game_state.game_stats["scenes_visited"] += 1
    
    # Display scene text
    print(scene["text"])
    
    # If the scene has choices, get player input
    if scene["choices"]:
        choices = list(scene["choices"].keys())
        player_choice = get_user_choice("What do you choose?", choices)
        
        # Handle special commands
        if player_choice in ['save', 'load', 'quit', 'help', 'stats']:
            if handle_special_command(player_choice):
                return "quit"
            return scene_name  # Stay in current scene
        
        # Record the choice
        game_state.player_choices.append(player_choice)
        game_state.game_stats["choices_made"] += 1
        
        # Return the next scene name
        return scene["choices"][player_choice]
    
    # If no choices, this is an ending scene
    return None

# MAIN GAME LOOP
def game_loop():
    """Main game loop that handles the flow of the game."""
    while game_state.current_scene:
        clear_screen()
        
        # Show game header
        print(f"🎮 {GAME_TITLE} | Scene: {game_state.current_scene}")
        print_separator()
        
        # Display current scene and get next scene
        next_scene = display_scene(game_state.current_scene)
        
        # Handle scene transitions
        if next_scene == "quit":
            break
        elif next_scene is None:
            # Game ended
            show_game_over()
            break
        else:
            # Continue to next scene
            game_state.current_scene = next_scene
            wait_for_input("\nPress Enter to continue...")
    
    return True

def show_game_over():
    """Display game over screen with statistics."""
    clear_screen()
    print("🎊 GAME COMPLETED! 🎊")
    print_separator("=")
    
    # Calculate game duration
    start_time = datetime.fromisoformat(game_state.game_stats["start_time"])
    duration = datetime.now() - start_time
    
    print(f"🏆 Final Statistics:")
    print(f"   Total Scenes Visited: {game_state.game_stats['scenes_visited']}")
    print(f"   Total Choices Made: {game_state.game_stats['choices_made']}")
    print(f"   Game Duration: {str(duration).split('.')[0]}")
    print(f"   Final Scene: {game_state.current_scene}")
    
    if game_state.player_choices:
        print(f"\n📜 Your Journey:")
        for i, choice in enumerate(game_state.player_choices, 1):
            print(f"   {i}. {choice}")
    
    print_separator("=")
    print("Thank you for playing Project Icarus!")

# MAIN MENU
def show_main_menu():
    """Display the main menu and handle user selection."""
    while True:
        print_title()
        print("🎮 MAIN MENU")
        print_separator()
        print("1. Start New Game")
        print("2. Load Saved Game")
        print("3. Help")
        print("4. Exit")
        print_separator()
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Start new game
            game_state.__init__()  # Reset game state
            print(f"\n🌟 Welcome to {GAME_TITLE}!")
            wait_for_input("Press Enter to begin your adventure...")
            return True
        elif choice == '2':
            # Load saved game
            if load_game():
                print(f"\n🔄 Game loaded! Continuing from scene: {game_state.current_scene}")
                wait_for_input("Press Enter to continue...")
                return True
            else:
                wait_for_input("Press Enter to return to menu...")
        elif choice == '3':
            # Show help
            clear_screen()
            show_help()
            wait_for_input("Press Enter to return to menu...")
        elif choice == '4':
            # Exit
            print(f"\nThanks for playing {GAME_TITLE}!")
            return False
        else:
            print("❌ Invalid choice. Please enter 1-4.")
            time.sleep(2)

# MAIN FUNCTION
def main():
    """Main function to start the game."""
    try:
        if show_main_menu():
            game_loop()
    except KeyboardInterrupt:
        print(f"\n\n👋 Game interrupted. Thanks for playing {GAME_TITLE}!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please report this issue!")

# START GAME
if __name__ == "__main__":
    main()
