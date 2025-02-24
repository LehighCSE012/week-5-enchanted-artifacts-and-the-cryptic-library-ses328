import random

def display_player_status(player_stats):
    """Displays the player's current health and attack."""
    print(f"\nPlayer Stats: Health = {player_stats['health']}, Attack = {player_stats['attack']}")

def display_inventory(inventory):
    """Displays the player's inventory."""
    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Inventory is empty.")

def acquire_item(inventory, item):
    """Adds an item to the player's inventory."""
    if item:
        inventory.append(item)
        print(f"You acquired: {item}")

def handle_path_choice(player_stats):
    """Handles player's choice when selecting a path."""
    return player_stats

def combat_encounter(player_stats, monster_health, has_treasure):
    """Handles combat between the player and a monster."""
    while monster_health > 0 and player_stats['health'] > 0:
        print("You attack the monster!")
        monster_health -= player_stats['attack']
        if monster_health <= 0:
            print("You defeated the monster!")
            return has_treasure
        print("The monster attacks!")
        player_stats['health'] -= 10
        display_player_status(player_stats)
    return None

def check_for_treasure(has_treasure):
    """Checks if the player has obtained treasure."""
    if has_treasure:
        print("You found a treasure chest!")
    else:
        print("No treasure here.")

def discover_artifact(player_stats, artifacts, artifact_name):
    """Handles the discovery of an artifact."""
    if artifact_name in artifacts:
        artifact = artifacts.pop(artifact_name)
        print(f"You found {artifact_name}: {artifact['description']}")
        if artifact['effect'] == "increases health":
            player_stats['health'] += artifact['power']
        elif artifact['effect'] == "enhances attack":
            player_stats['attack'] += artifact['power']
        print(f"Effect: {artifact['effect']} (+{artifact['power']})")
    else:
        print("You found nothing of interest.")
    return player_stats, artifacts

def find_clue(clues, new_clue):
    """Handles the discovery of a clue."""
    if new_clue in clues:
        print("You already know this clue.")
    else:
        clues.add(new_clue)
        print(f"You discovered a new clue: {new_clue}")
    return clues

def enter_dungeon(player_stats, inventory, dungeon_rooms, clues):
    """Handles the player's exploration of the dungeon."""
    for room_name, item, challenge_type, _ in dungeon_rooms:
        print(f"\nYou entered: {room_name}")
        acquire_item(inventory, item)
        if challenge_type == "library":
            print("A vast library filled with ancient, cryptic texts.")
            possible_clues = [
                "The treasure is hidden where the dragon sleeps.",
                "The key lies with the gnome.",
                "Beware the shadows.",
                "The amulet unlocks the final door."
            ]
            new_clues = random.sample(possible_clues, 2)
            for clue in new_clues:
                clues = find_clue(clues, clue)
            if "staff_of_wisdom" in inventory:
                print("With the Staff of Wisdom, you understand the meaning of these clues and can bypass a puzzle!")
    return player_stats, inventory, clues

def main():
    """Main game loop."""
    dungeon_rooms = [
        ("Dusty library", "key", "puzzle", ("Solved puzzle!", "Puzzle unsolved.", -5)),
        ("Narrow passage, creaky floor", "torch", "trap", ("Avoided trap!", "Triggered trap!", -10)),
        ("Grand hall, shimmering pool", "healing potion", "none", None),
        ("Small room, locked chest", "treasure", "puzzle", ("Cracked code!", "Chest locked.", -5)),
        ("Cryptic Library", None, "library", None)
    ]
    player_stats = {'health': 100, 'attack': 5}
    monster_health = 70
    inventory = []
    clues = set()
    artifacts = {
        "amulet_of_vitality": {"description": "Glowing amulet, life force.", "power": 15, "effect": "increases health"},
        "ring_of_strength": {"description": "Powerful ring, attack boost.", "power": 10, "effect": "enhances attack"},
        "staff_of_wisdom": {"description": "Staff of wisdom, ancient.", "power": 5, "effect": "solves puzzles"}
    }
    has_treasure = random.choice([True, False])
    display_player_status(player_stats)
    player_stats = handle_path_choice(player_stats)
    if player_stats['health'] > 0:
        treasure_obtained_in_combat = combat_encounter(player_stats, monster_health, has_treasure)
        if treasure_obtained_in_combat:
            check_for_treasure(treasure_obtained_in_combat)
        if random.random() < 0.3:
            artifact_keys = list(artifacts.keys())
            if artifact_keys:
                artifact_name = random.choice(artifact_keys)
                player_stats, artifacts = discover_artifact(player_stats, artifacts, artifact_name)
                display_player_status(player_stats)
        if player_stats['health'] > 0:
            player_stats, inventory, clues = enter_dungeon(player_stats, inventory, dungeon_rooms, clues)
            print("\n--- Game End ---")
            display_player_status(player_stats)
            print("Final Inventory:")
            display_inventory(inventory)
            print("Clues:")
            if clues:
                for clue in clues:
                    print(f"- {clue}")
            else:
                print("No clues.")

if __name__ == "__main__":
    main()
