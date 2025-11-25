# BENZOS STATION EXODUS

A text-based adventure game where you navigate through a space station, exploring different rooms and collecting items.

## 📖 Description

This program allows a player to move between rooms using **directional commands**. The game features:
- A dictionary for the simplified space station text game
- The dictionary links a room to other rooms based on directional commands
- A dictionary to store items in each room
- **Note:** This is a simplified version for the milestone - full game will have all 8 rooms

## 🎮 How to Play

### Commands
- `go [direction]` - Move to an adjacent room (North, South, East, West)
- `get` - Pick up items in the current room
- `exit` - Quit the game

### Game Map
```
        [Medical Bay]
              |
    [Command Center] --- [Medical Bay]
              |
    [Living Quarters] --- [Engineering Workshop]
```

## 🚀 Installation & Running

### Prerequisites
- Python 3.x installed on your system

### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/BENZOS-STATION-EXODUS.git
   ```

2. Navigate to the project directory:
   ```bash
   cd BENZOS-STATION-EXODUS
   ```

3. Run the game:
   ```bash
   python TextBasedGame.py
   ```

## 🎯 Game Features

- **Room Navigation**: Move between connected rooms using directional commands
- **Inventory System**: Collect items from different rooms
- **Input Validation**: The game validates your commands and provides helpful feedback
- **Status Display**: Always see your current location and inventory

## 📦 Items Available

- **Command Center**: Keycard
- **Living Quarters**: First Aid Kit
- **Medical Bay**: Medkit
- **Engineering Workshop**: Wrench

## 🛠️ Technical Details

- Written in Python 3
- Uses dictionaries for room connections and item storage
- Implements function-based game logic
- Input validation for user commands

## 📝 Project Information

**Course**: Southern New Hampshire University - Cybersecurity Program  
**Developer**: Benjamin Williams  
**Project Type**: Text-Based Game / Python Programming

## 🔮 Future Enhancements

- Add more rooms (expanding to full 8-room station)
- Implement win/lose conditions
- Add enemy encounters
- Create more complex item interactions
- Add save/load game functionality

## 📄 License

This project is part of an educational assignment.

---

*Safe travels through Benzos Station, astronaut! 🚀*
