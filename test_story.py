#!/usr/bin/env python3
"""
Test script to validate the story structure and flow
"""

from scenes import scenes

def test_story_structure():
    """Test that all scenes are properly connected"""
    print("🧪 Testing Story Structure...")
    print("=" * 50)
    
    # Test 1: Check that all scenes exist
    print(f"✅ Total scenes loaded: {len(scenes)}")
    
    # Test 2: Check that opening scene exists
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
    print(f"✅ Found {len(endings)} ending scenes:")
    for ending in endings:
        print(f"   - {ending}")
    
    # Test 5: Check for unreachable scenes
    reachable = set(["opening"])
    to_check = ["opening"]
    
    while to_check:
        current = to_check.pop(0)
        if current in scenes:
            for choice, next_scene in scenes[current].get("choices", {}).items():
                if next_scene not in reachable:
                    reachable.add(next_scene)
                    to_check.append(next_scene)
    
    unreachable = set(scenes.keys()) - reachable
    if unreachable:
        print(f"⚠️  Warning: {len(unreachable)} unreachable scenes:")
        for scene in unreachable:
            print(f"   - {scene}")
    else:
        print("✅ All scenes are reachable")
    
    print("\n🎮 Story Paths Summary:")
    print("=" * 50)
    print("Main starting paths from opening:")
    for choice, next_scene in scenes["opening"]["choices"].items():
        print(f"   {choice} → {next_scene}")
    
    print("\nSample story flow:")
    print("opening → beach_search → message_bottle → hidden_harbor → honorable_escape")
    
    return True

def test_scene_content():
    """Test that scenes have proper content"""
    print("\n📝 Testing Scene Content...")
    print("=" * 50)
    
    issues = []
    
    for scene_name, scene_data in scenes.items():
        # Check required fields
        if "text" not in scene_data:
            issues.append(f"{scene_name}: Missing 'text' field")
        elif not scene_data["text"].strip():
            issues.append(f"{scene_name}: Empty text content")
        
        if "choices" not in scene_data:
            issues.append(f"{scene_name}: Missing 'choices' field")
        
        # Check ending scenes
        if not scene_data.get("choices"):
            if "THE END" not in scene_data.get("text", ""):
                issues.append(f"{scene_name}: Ending scene missing 'THE END' marker")
    
    if issues:
        print("❌ Content issues found:")
        for issue in issues:
            print(f"   {issue}")
        return False
    else:
        print("✅ All scenes have proper content structure")
        return True

if __name__ == "__main__":
    print("🎯 Project Icarus - Story Validation Test")
    print("=" * 60)
    
    structure_ok = test_story_structure()
    content_ok = test_scene_content()
    
    print("\n🏆 FINAL RESULTS:")
    print("=" * 60)
    if structure_ok and content_ok:
        print("✅ All tests passed! The story is ready to play.")
        print("\n🎮 To start the game, run: python main.py")
        print("\n💡 The story includes:")
        print("   - Multiple branching paths")
        print("   - Several different endings")
        print("   - Character interactions")
        print("   - Exploration elements")
        print("   - Meaningful choices with consequences")
    else:
        print("❌ Some tests failed. Please check the issues above.")
