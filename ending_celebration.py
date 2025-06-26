#!/usr/bin/env python3
"""
Show all possible endings in the story
"""

from scenes import scenes

def show_ending_celebration():
    """Show the ending the user just achieved with celebration"""
    print("🎊" * 60)
    print("🏆 CONGRATULATIONS! GAME COMPLETED! 🏆")
    print("🎊" * 60)
    
    # Show the specific ending
    ending = scenes["quick_escape"]
    text = ending["text"]
    
    print("\n🎯 YOU ACHIEVED: The Practical Escape")
    print("🏅 ENDING TYPE: Survivor")
    print("📍 FINAL LOCATION: Open Ocean")
    
    # Extract the achievement line
    for line in text.split('\n'):
        if "🎊 You have achieved" in line:
            print(f"🎊 {line.strip()}")
            break
    
    print("\n📖 YOUR ENDING STORY:")
    print("-" * 50)
    # Show the key parts of the ending
    lines = text.split('\n')
    for line in lines:
        if line.strip() and not line.startswith('🎊') and 'THE END' not in line:
            print(f"   {line}")
    print("-" * 50)
    
    print("\n🗺️  YOUR PATH: opening → investigate campfire → build escape raft")
    
def show_all_possible_endings():
    """Show all endings the user could discover"""
    endings = [scene for scene, data in scenes.items() if not data.get("choices")]
    
    print("\n" + "🌟" * 60)
    print("🎮 ALL POSSIBLE ENDINGS TO DISCOVER")
    print("🌟" * 60)
    
    # Categorize endings
    categories = {
        'wisdom': ['🧠 WISDOM & KNOWLEDGE ENDINGS', []],
        'scholar': ['🧠 WISDOM & KNOWLEDGE ENDINGS', []],
        'universal_wisdom': ['🧠 WISDOM & KNOWLEDGE ENDINGS', []],
        'generosity': ['💖 VALUES & GENEROSITY ENDINGS', []],
        'realization': ['💖 VALUES & GENEROSITY ENDINGS', []],
        'true_wealth': ['💖 VALUES & GENEROSITY ENDINGS', []],
        'service': ['🤝 COMMUNITY & SERVICE ENDINGS', []],
        'divine_service': ['🤝 COMMUNITY & SERVICE ENDINGS', []],
        'discovery': ['🔍 EXPLORATION & DISCOVERY ENDINGS', []],
        'independence': ['🔍 EXPLORATION & DISCOVERY ENDINGS', []],
        'survivor': ['🛡️ SURVIVAL & PRACTICAL ENDINGS', []]
    }
    
    # Sort endings into categories
    for ending in endings:
        ending_type = scenes[ending]["metadata"].get("ending_type", "unknown")
        ending_data = scenes[ending]
        
        # Extract title and achievement
        text = ending_data["text"]
        title = ""
        achievement = ""
        
        for line in text.split('\n'):
            if line.strip().startswith("THE END"):
                title = line.strip().replace("THE END - ", "")
            elif "🎊 You have achieved" in line:
                achievement = line.strip()
        
        # Add to appropriate category
        for cat_key, (cat_name, cat_list) in categories.items():
            if ending_type == cat_key or cat_key in ending_type:
                cat_list.append((ending, title, achievement))
                break
    
    # Display categories
    for cat_name, cat_endings in categories.values():
        if cat_endings:
            print(f"\n{cat_name}")
            print("─" * 40)
            for ending_id, title, achievement in cat_endings:
                status = "✅ COMPLETED!" if ending_id == "quick_escape" else "🔍 Not yet discovered"
                print(f"   • {title}")
                print(f"     {achievement}")
                print(f"     {status}")
                print()

def show_replay_suggestions():
    """Suggest different paths to try"""
    print("\n" + "🎯" * 60)
    print("🎮 WANT TO DISCOVER MORE ENDINGS?")
    print("🎯" * 60)
    
    print("\n🗺️  Try these different starting choices:")
    print("   🕳️  Explore Cave → Discover ancient treasures and temples")
    print("   🌿 Enter Jungle → Meet Marcus and choose your philosophy")
    print("   🔥 Investigate Campfire → Multiple paths including your current one")
    
    print("\n🎪 Different choices lead to different adventures:")
    print("   • Seek wisdom and become a teacher")
    print("   • Find treasure but learn about true wealth")
    print("   • Join a community of island guardians")
    print("   • Discover ancient temples with mystical tests")
    print("   • Help other castaways and find purpose")
    
    print("\n💡 Pro tip: Each ending teaches something valuable about life!")

if __name__ == "__main__":
    show_ending_celebration()
    show_all_possible_endings()
    show_replay_suggestions()
    
    print("\n" + "🎊" * 60)
    print("Thank you for playing Project Icarus!")
    print("🎮 Run 'python main.py' to play again with different choices!")
    print("🎊" * 60)
