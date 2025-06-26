#!/usr/bin/env python3
"""
Test script for the simplified story - now with ending analysis
"""

from scenes import scenes

def test_simple_story():
    """Test the simplified story structure"""
    print("🧪 Testing Simplified Story Structure...")
    print("=" * 50)
    
    # Test 1: Check basic structure
    print(f"✅ Total scenes loaded: {len(scenes)}")
    
    # Test 2: Check opening scene exists
    if "opening" in scenes:
        print("✅ Opening scene found")
    else:
        print("❌ Opening scene missing!")
        return False
    
    # Test 3: Check for broken links
    broken_links = []
    for scene_name, scene_data in scenes.items():
        for choice, next_scene in scene_data.get("choices", {}).items():
            if next_scene not in scenes:
                broken_links.append(f"{scene_name} -> {choice} -> {next_scene}")
    
    if broken_links:
        print("❌ Broken scene links found:")
        for link in broken_links:
            print(f"   {link}")
        return False
    else:
        print("✅ All scene links are valid")
    
    # Test 4: Count endings
    endings = [scene for scene, data in scenes.items() if not data.get("choices")]
    print(f"✅ Found {len(endings)} ending scenes")
    
    # Test 5: Show story paths
    print("\n🎮 Story Overview:")
    print("=" * 50)
    print("Starting choices from opening scene:")
    for choice, next_scene in scenes["opening"]["choices"].items():
        print(f"   {choice} → {next_scene}")
    
    print(f"\nTotal possible endings: {len(endings)}")
    print("Sample endings:")
    for ending in endings[:5]:
        ending_type = scenes[ending]["metadata"].get("ending_type", "unknown")
        print(f"   - {ending} ({ending_type})")
    
    return True

def analyze_ending(ending_name):
    """Analyze and display detailed information about a specific ending"""
    if ending_name not in scenes:
        print(f"❌ Ending '{ending_name}' not found!")
        return
    
    ending = scenes[ending_name]
    
    print("\n" + "�" * 60)
    print("🏆 ENDING ANALYSIS")
    print("🎊" * 60)
    
    # Extract ending information from the text
    text = ending["text"]
    lines = text.split('\n')
    
    # Find the "THE END" line and ending type
    ending_title = ""
    ending_description = ""
    
    for line in lines:
        if line.strip().startswith("THE END"):
            ending_title = line.strip()
        elif "🎊 You have achieved" in line:
            ending_description = line.strip()
    
    print(f"🎯 Ending: {ending_name}")
    print(f"📜 Title: {ending_title}")
    print(f"🏅 Achievement: {ending_description}")
    
    # Show ending type from metadata
    ending_type = ending["metadata"].get("ending_type", "unknown")
    location = ending["metadata"].get("location", "unknown")
    
    print(f"🏷️  Type: {ending_type}")
    print(f"📍 Final Location: {location}")
    
    print("\n📖 Full Ending Text:")
    print("-" * 50)
    print(text)
    print("-" * 50)
    
    # Show path analysis
    print("\n🗺️  How to reach this ending:")
    paths_to_ending = find_paths_to_scene(ending_name)
    if paths_to_ending:
        for i, path in enumerate(paths_to_ending[:3], 1):  # Show first 3 paths
            print(f"   Path {i}: {' → '.join(path)}")
    
    print("🎊" * 60)

def find_paths_to_scene(target_scene, current_scene="opening", path=None, visited=None):
    """Find all paths from opening to a target scene"""
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    if current_scene in visited:
        return []
    
    visited = visited.copy()
    visited.add(current_scene)
    path = path + [current_scene]
    
    if current_scene == target_scene:
        return [path]
    
    if current_scene not in scenes:
        return []
    
    all_paths = []
    for choice, next_scene in scenes[current_scene].get("choices", {}).items():
        paths = find_paths_to_scene(target_scene, next_scene, path, visited)
        all_paths.extend(paths)
    
    return all_paths

def show_all_endings():
    """Show all available endings with their types"""
    endings = [scene for scene, data in scenes.items() if not data.get("choices")]
    
    print("\n🎊 ALL AVAILABLE ENDINGS")
    print("=" * 60)
    
    by_type = {}
    for ending in endings:
        ending_type = scenes[ending]["metadata"].get("ending_type", "unknown")
        if ending_type not in by_type:
            by_type[ending_type] = []
        by_type[ending_type].append(ending)
    
    for ending_type, ending_list in sorted(by_type.items()):
        print(f"\n🏷️  {ending_type.upper()} ENDINGS:")
        for ending in ending_list:
            # Extract achievement line
            text = scenes[ending]["text"]
            achievement = ""
            for line in text.split('\n'):
                if "🎊 You have achieved" in line:
                    achievement = line.strip()
                    break
            print(f"   • {ending}: {achievement}")

def interactive_menu():
    """Interactive menu for ending analysis"""
    while True:
        print("\n🎮 ENDING ANALYZER MENU")
        print("=" * 40)
        print("1. Test story structure")
        print("2. Show all endings")
        print("3. Analyze specific ending")
        print("4. Show ending you just got (quick_escape)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            test_simple_story()
        elif choice == '2':
            show_all_endings()
        elif choice == '3':
            ending_name = input("Enter ending scene name: ").strip()
            analyze_ending(ending_name)
        elif choice == '4':
            print("\n🎯 YOUR RECENT ENDING:")
            analyze_ending("quick_escape")
        elif choice == '5':
            print("👋 Thanks for using the Ending Analyzer!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    print("🎯 Project Icarus - Story Analyzer")
    print("=" * 60)
    
    # Show the specific ending the user just experienced
    print("🎊 CONGRATULATIONS! You just completed the game!")
    print("Let's analyze the ending you achieved...")
    analyze_ending("quick_escape")
    
    # Offer interactive menu
    print("\n" + "="*60)
    print("Would you like to explore more about the story?")
    explore = input("Enter 'y' for interactive menu, or any other key to exit: ").strip().lower()
    
    if explore == 'y':
        interactive_menu()
    else:
        print("\n🎮 Thanks for playing Project Icarus!")
        print("💡 Try playing again with different choices to discover other endings!")
