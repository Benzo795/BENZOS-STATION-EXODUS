# BENZOS STATION EXODUS
Text Based Game
# This program allows a player to move between rooms using directional commands

# A dictionary for the simplified space station text game
# The dictionary links a room to other rooms based on Gabes Station Exodus design
# Note: This is a simplified version for the milestone - full game will have all 8 rooms
rooms = {
    'Command Center': {'South': 'Living Quarters', 'East': 'Medical Bay'},
    'Living Quarters': {'North': 'Command Center', 'East': 'Engineering Workshop'},
    'Medical Bay': {'West': 'Command Center', 'South': 'Engineering Workshop'},
    'Engineering Workshop': {'North': 'Medical Bay', 'West': 'Living Quarters'}
}

# Dictionary to store items in each room
room_items = {
    'Command Center': [],
    'Living Quarters': ['Access Card'],
    'Medical Bay': ['Medkit'],
    'Engineering Workshop': ['Repair Tools']
}


def show_instructions():
    """Display game instructions to the player"""
    print("=" * 60)
    print("Welcome to Gabes Station Exodus - Simplified Version")
    print("=" * 60)
    print("You are a lone astronaut on an abandoned space station.")
    print("Navigate between rooms using directional commands.")
    print()
    print("Commands:")
    print("- go North, go South, go East, go West (to move between rooms)")
    print("- get (to pick up items)")
    print("- exit (to quit the game)")
    print("=" * 60)


def show_status(current_room, inventory):
    """Display the player's current location, available directions, and items"""
    print(f"\nYou are in the {current_room}")

    # Add room descriptions for immersion
    room_descriptions = {
        'Command Center': "The main control hub of the station. Control panels flicker with emergency lighting.",
        'Living Quarters': "Personal quarters with floating belongings scattered about in zero gravity.",
        'Medical Bay': "The station's medical facility with equipment floating freely.",
        'Engineering Workshop': "Technical area filled with repair tools and machinery."
    }

    print(room_descriptions.get(current_room, "A room on the space station."))

    # Show items in current room
    if room_items[current_room]:
        items_here = ', '.join(room_items[current_room])
        print(f"Items here: {items_here}")

    # Show available directions
    available_directions = list(rooms[current_room].keys())
    if available_directions:
        print(f"Available directions: {', '.join(available_directions)}")

    # Show inventory
    if inventory:
        inventory_list = ', '.join(inventory)
        print(f"Inventory: {inventory_list}")
    else:
        print("Inventory: Empty")

    print("-" * 40)


def get_item(current_room, inventory):
    """
    Handle item pickup in current room
    Returns: updated inventory
    """
    if not room_items[current_room]:
        print("\nThere are no items to pick up in this room.")
        return inventory

    item_name = room_items[current_room][0]  # Get first item in room
    print(f"\nYou see a {item_name} in this room.")
    choice = input(f"Do you want to pick up the {item_name}? (yes/no): ").strip().lower()

    if choice == 'yes' or choice == 'y':
        # Remove item from room and add to inventory
        room_items[current_room].remove(item_name)
        inventory.append(item_name)
        print(f"\nYou picked up the {item_name}.")

        # Check if player has collected all items
        if len(inventory) == 3:  # Total items in simplified version
            print("\nGreat! You've collected several essential items for your escape!")

    elif choice == 'no' or choice == 'n':
        print(f"\nYou leave the {item_name} where it is.")
    else:
        print("\nInvalid input. Please answer 'yes' or 'no'.")

    return inventory


def validate_move_command(command, current_room):
    """
    Validate and process movement commands
    Returns: (is_valid, direction, error_message)
    """
    # Parse the command
    command_parts = command.split()

    # Check command format
    if len(command_parts) != 2:
        return False, None, "Invalid command format! Use: 'go [direction]'"

    if command_parts[0].lower() != 'go':
        return False, None, "Invalid command! Use 'go [direction]' to move or 'exit' to quit."

    # Get and validate direction
    direction = command_parts[1].title()  # Capitalize first letter (North, South, etc.)

    # Check if direction is valid for current room
    if direction not in rooms[current_room]:
        available = ', '.join(rooms[current_room].keys())
        return False, None, f"You can't go {direction} from here! Available directions: {available}"

    return True, direction, None


def main():
    """Main game loop with decision branching and room navigation"""
    # Starting room - Command Center as specified in design document
    current_room = 'Command Center'

    # Player inventory to store collected items
    inventory = []

    # Display game instructions
    show_instructions()

    # Main gameplay loop
    while True:
        # Display current status
        show_status(current_room, inventory)

        # Get player input
        user_input = input("Enter your command: ").strip()

        # Decision branching for different commands
        if user_input.lower() == 'exit':
            # Exit command - end the game
            print("\nExiting Gabes Station Exodus...")
            print("Thanks for playing! Safe travels, astronaut!")
            break

        elif user_input.lower().startswith('go'):
            # Movement command - validate and process
            is_valid, direction, error_message = validate_move_command(user_input, current_room)

            if is_valid:
                # Valid move - update current room using dictionary
                new_room = rooms[current_room][direction]
                print(f"\nYou move {direction.lower()} through the station corridors...")
                current_room = new_room
            else:
                # Invalid move - display error message
                print(f"\n{error_message}")

        elif user_input.lower() == 'get':
            # Item pickup command
            inventory = get_item(current_room, inventory)

        else:
            # Invalid command - input validation
            print("\nInvalid command!")
            print("Valid commands:")
            print("- 'go [direction]' (North, South, East, West)")
            print("- 'get' (to pick up items)")
            print("- 'exit' (to quit)")


# Run the game when script is executed
if __name__ == "__main__":
    main()