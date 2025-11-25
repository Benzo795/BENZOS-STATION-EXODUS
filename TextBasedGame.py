"""
BENZOS STATION EXODUS - Text Based Game
A text-based adventure game where players navigate through a space station.
"""

# Dictionary to store items in each room
inventory = []

# Dictionary for the simplified space station text game
# The dictionary links a room to other rooms based on directional commands
rooms = {
    'Command Center': {'South': 'Living Quarters', 'East': 'Medical Bay'},
    'Living Quarters': {'North': 'Command Center', 'East': 'Engineering Workshop'},
    'Medical Bay': {'West': 'Command Center', 'South': 'Engineering Workshop'},
    'Engineering Workshop': {'North': 'Medical Bay', 'West': 'Living Quarters'}
}

# Dictionary to store items in each room
room_items = {
    'Command Center': 'Keycard',
    'Living Quarters': 'First Aid Kit',
    'Medical Bay': 'Medkit',
    'Engineering Workshop': 'Wrench'
}

# Starting room
current_room = 'Command Center'


def show_status():
    """Display the player's current status including room and inventory"""
    print('\n' + '=' * 50)
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    
    # Show available items in the room
    if current_room in room_items:
        print(f'You see: {room_items[current_room]}')
    
    print('=' * 50)


def get_item(current_room, inventory):
    """Handle item pickup in the current room"""
    if current_room in room_items:
        item = room_items[current_room]
        inventory.append(item)
        print(f'\nYou picked up: {item}')
        del room_items[current_room]  # Remove item from room after pickup
    else:
        print('\nThere is nothing to pick up here.')
    return inventory


def validate_move_command(user_input, current_room):
    """Validate the movement command and return validity, direction, and error message"""
    # Check if it's a valid 'go' command
    if not user_input.lower().startswith('go '):
        return False, None, "Invalid command! Use 'go [direction]'"
    
    # Extract direction from command
    direction = user_input[3:].strip().title()
    
    # Check if direction is valid for current room
    if direction not in rooms[current_room]:
        return False, None, f"You can't go {direction} from here!"
    
    return True, direction, None


def main():
    """Main game loop"""
    global current_room
    
    print('=' * 50)
    print('BENZOS STATION EXODUS')
    print('=' * 50)
    print('\nWelcome to Benzos Station Exodus!')
    print('Navigate through the space station and collect items.')
    print('\nCommands:')
    print('  - go [direction]: Move (North, South, East, West)')
    print('  - get: Pick up items')
    print('  - exit: Quit the game')
    print('=' * 50)
    
    # Show initial status
    show_status()
    
    # Game loop
    while True:
        # Get player input
        user_input = input('Enter your command: ').strip()
        
        # Decision branching for different commands
        if user_input.lower() == 'exit':
            # Exit command - end the game
            print('\nExiting Benzos Station Exodus...')
            print('Thanks for playing! Safe travels, astronaut!')
            break
        
        elif user_input.lower().startswith('go'):
            # Movement command - validate and process
            is_valid, direction, error_message = validate_move_command(user_input, current_room)
            
            if is_valid:
                # Valid move - update current room using dictionary
                new_room = rooms[current_room][direction]
                print(f'\nYou move {direction.lower()} through the station corridors...')
                current_room = new_room
            else:
                # Invalid move - display error message
                print(f'\n{error_message}')
            
            # Show status after move attempt
            show_status()
        
        elif user_input.lower() == 'get':
            # Item pickup command
            inventory = get_item(current_room, inventory)
        
        else:
            # Invalid command - input validation
            print('\nInvalid command!')
            print('Valid commands:')
            print('  - go [direction]: (North, South, East, West)')
            print('  - get: (to pick up items)')
            print('  - exit: (to quit)')


# Run the game when script is executed
if __name__ == '__main__':
    main()
