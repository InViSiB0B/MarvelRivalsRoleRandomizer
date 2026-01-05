# Marvel Rivals Role Randomizer

A Python-based role randomizer for Marvel Rivals that assigns balanced team compositions for 6-player teams.

## Features

- Random role assignment for 6 players
- Ensures balanced team composition following Marvel Rivals guidelines:
  - At least 2 Strategists (max 3)
  - At least 1 Vanguard
  - At least 1 Duelist
- Sound effects when randomizing roles
- Easy-to-read role assignments grouped by role type
- Ability to re-randomize until you get a composition your team likes
- Support for changing players mid-session

## Requirements

- Python 3.7+
- pygame (for sound effects)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/MarvelRivalsRoleRandomizer.git
cd MarvelRivalsRoleRandomizer
```

2. Install dependencies:
```bash
pip install pygame
```

3. Run the application:
```bash
python main.py
```

## Usage

1. Launch the program
2. Enter the names of all 6 players when prompted
3. Choose from the menu:
   - **Randomize roles**: Generate a balanced team composition
   - **Add new players**: Change the player roster
   - **Quit**: Exit the application

4. When viewing role assignments, you can keep randomizing until you find a composition your team wants to try

### Example Output

```
==================================================
MARVEL RIVALS TEAM ASSIGNMENT
==================================================

🛡️ VANGUARD:
  • Player1
  • Player2

⚔️ DUELIST:
  • Player3

🧠 STRATEGIST:
  • Player4
  • Player5
  • Player6

==================================================
```

## Roles

- **Vanguard** 🛡️: Tanky heroes who lead the charge
- **Duelist** ⚔️: Damage dealers who eliminate threats
- **Strategist** 🧠: Support heroes who heal and enable the team

## Building an Executable

You can build a standalone executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "again.mp3;." main.py
```

The executable will be in the `dist` folder.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built for the Marvel Rivals community
- Sound effects enhance the randomization experience
