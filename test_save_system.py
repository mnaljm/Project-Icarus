#!/usr/bin/env python3
"""
Test the save/load system for Project Icarus
"""

import os
import json
from pathlib import Path

# Test the save directory creation
def test_save_system():
    print("🧪 Testing Save System...")
    print("=" * 50)
    
    # Create the same save directory structure as the game
    saves_dir = Path.home() / "Documents" / "ProjectIcarus" / "saves"
    save_file = saves_dir / "test_save.json"
    
    print(f"📁 Save directory: {saves_dir}")
    print(f"💾 Test save file: {save_file}")
    
    # Test directory creation
    try:
        saves_dir.mkdir(parents=True, exist_ok=True)
        print("✅ Save directory created/verified")
    except Exception as e:
        print(f"❌ Failed to create save directory: {e}")
        return False
    
    # Test file writing
    try:
        test_data = {
            "test": "data",
            "player_name": "TestPlayer",
            "current_scene": "opening"
        }
        
        with open(save_file, 'w') as f:
            json.dump(test_data, f, indent=2)
        
        print("✅ Successfully wrote test save file")
    except Exception as e:
        print(f"❌ Failed to write save file: {e}")
        return False
    
    # Test file reading
    try:
        with open(save_file, 'r') as f:
            loaded_data = json.load(f)
        
        if loaded_data == test_data:
            print("✅ Successfully read and verified save file")
        else:
            print("❌ Save file data doesn't match")
            return False
    except Exception as e:
        print(f"❌ Failed to read save file: {e}")
        return False
    
    # Clean up test file
    try:
        save_file.unlink()
        print("✅ Test file cleaned up")
    except Exception as e:
        print(f"⚠️  Warning: Could not clean up test file: {e}")
    
    print("\n🎉 Save system test completed successfully!")
    print(f"📍 Your saves will be stored in: {saves_dir}")
    return True

if __name__ == "__main__":
    print("🎯 Project Icarus - Save System Test")
    print("=" * 60)
    
    if test_save_system():
        print("\n✅ Save system is working correctly!")
        print("🎮 You can now save your game progress safely.")
        print("\n💡 The game will save to your Documents folder:")
        saves_dir = Path.home() / "Documents" / "ProjectIcarus" / "saves"
        print(f"   {saves_dir}")
    else:
        print("\n❌ Save system has issues. Please check permissions.")
