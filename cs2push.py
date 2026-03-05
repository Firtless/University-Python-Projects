import random
import os

MAPS = {
    "Dust2": ["Mid", "A-Site", "B-Site", "Short", "Long", "Lower", "Tunnels", "Catwalk", "Pit", "Goose", "Xbox"],
    "Mirage": ["Mid", "A-Site", "B-Site", "Jungle", "Apps", "Lower", "Short", "Palace", "Tetris", "Window", "Connector", "Bench", "Van"],
    "Inferno": ["Mid", "A-Site", "B-Site", "Banana", "Apps", "Arch", "Pit", "Library", "Graveyard", "Construction", "Boiler"],
    "Nuke": ["Ramp", "A-Site", "B-Site", "Door", "Outside", "Vent", "Secret", "Roof", "Heaven", "Trophy", "Mini", "Garage"],
    "Overpass": ["Monster", "Pipe", "Construction", "B-Site", "A-Site", "Long", "Bathroom", "Party", "Connector", "Heaven", "Pit"],
    "Anubis": ["Canal", "Bridge", "Mid", "A-Site", "B-Site", "Water", "Ruins", "Connector", "Alley", "Heaven"],
    "Office": ["Front Office", "Kitchen", "Paper", "Long Hall", "Side Hall", "Projector", "Conference", "Garage", "Sniper Alley"],
    "Train": ["Green", "Popdog", "Olof", "Hell", "Ivy", "Connector", "A-Site", "B-Site", "Heaven", "Summit"],
    "Vertigo": ["Ramp", "A-Site", "B-Site", "Mid", "Backside", "Elevator", "Scaffold", "Sidewalk", "Bridge"],
    "Ancient": ["Mid", "A-Site", "B-Site", "Donut", "Temple", "Lane", "Cheetah", "Ruins", "Red Room", "Jaguar"]
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_pos(current_map, last_pos):
    positions = MAPS[current_map]
    choice = random.choice(positions)

    if choice == last_pos and len(positions) > 1:
        return get_random_pos(current_map, last_pos)
    return choice


def run_map_session(map_name):
    last_pos = None
    while True:
        clear_screen()
        print(f"=== CURRENT MAP: {map_name.upper()} ===")
        print(f"Last Position: {last_pos if last_pos else 'None'}")
        print("\n[S] Spin for new position")
        print("[B] Back to Map Menu")

        choice = input("\nAction: ").strip().lower()

        if choice == 's':
            last_pos = get_random_pos(map_name, last_pos)
            print(f"\n>>> RUSH: {last_pos} <<<")
            input("\nPress Enter to continue...")
        elif choice == 'b':
            break


def main():
    while True:
        clear_screen()
        print("=== CS2 TRUE RANDOMIZER ===")
        print("Available Maps:")
        for map_name in MAPS.keys():
            print(f"- {map_name}")
        print("\n[Type Map Name] to start")
        print("[Q] to Quit Program")

        user_input = input("\nSelection: ").strip().title()

        if user_input == 'Q':
            break
        elif user_input in MAPS:
            run_map_session(user_input)
        else:
            print(f"\nError: '{user_input}' is not in the list.")
            input("Press Enter to try again...")


if __name__ == "__main__":
    main()
