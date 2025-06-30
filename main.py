import random
import pygame
import os
import sys
from typing import List, Dict


def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MarvelRivalsRoleRandomizer:
    def __init__(self):
        self.players = []
        self.roles = ["Vanguard", "Duelist", "Strategist"]

        # Initialize pygame mixer for sound
        pygame.mixer.init()
        self.sound_file = "again.mp3"  # Primary path (for development)
        self.sound_file_fallback = get_resource_path("again.mp3")  # Fallback (for exe)

    def play_sound(self):
        """Play the randomize sound effect"""
        try:
            # Try the primary path first (development environment)
            if os.path.exists(self.sound_file):
                pygame.mixer.music.load(self.sound_file)
                pygame.mixer.music.play()
            # If that fails, try the PyInstaller bundled path
            elif os.path.exists(self.sound_file_fallback):
                pygame.mixer.music.load(self.sound_file_fallback)
                pygame.mixer.music.play()
            else:
                print(f"Sound file not found in either location!")
        except Exception as e:
            print(f"Could not play sound: {e}")


    def add_players(self, player_names: List[str]):
        """Add player names to the game"""
        if len(player_names) != 6:
            raise ValueError("Exactly 6 players are required!")
        self.players = player_names

    def generate_role_assignment(self) -> Dict[str, str]:
        """
        Generate a random role assignment that follows the rules:
        - At least 2 Strategists, but no more than 3
        - At least 1 Vanguard
        - At least 1 Duelist
        """
        if len(self.players) != 6:
            raise ValueError("Must have exactly 6 players!")
        
        # Start with minimum required roles
        assignment = ["Strategist", "Strategist", "Vanguard", "Duelist"]

        # Fill remaining 2 slots with constraing on max Strategists
        remaining_slots = 2
        for _ in range(remaining_slots):
            # Count current strategists
            strategist_count = assignment.count("Strategist")

            # If we already have 3 strategists, choose from other roles
            if strategist_count >= 3:
                available_roles = ["Vanguard", "Duelist"]
            else:
                available_roles = self.roles

            assignment.append(random.choice(available_roles))
        
        # Shuffle the assignments
        random.shuffle(assignment)

        # Create player-role mapping
        return dict(zip(self.players, assignment))
    
    def display_assignment(self, assignment: Dict[str, str]):
        """Display the role assignments in a formatted way"""
        print("\n" + "="*50)
        print("MARVEL RIVALS TEAM ASSIGNMENT")
        print("="*50)

        # Group by roles for better display
        role_groups = {"Vanguard": [], "Duelist": [], "Strategist": []}

        for player, role in assignment.items():
            role_groups[role].append(player)

        for role, players in role_groups.items():
            if players: # Only show roles that have players
                emoji = {"Vanguard": "🛡️", "Duelist": "⚔️", "Strategist": "🧠"}
                print(f"\n{emoji[role]} {role.upper()}:")
                for player in players:
                    print(f"  • {player}")
        
        print("\n" + "="*50)

def main():
    randomizer = MarvelRivalsRoleRandomizer()

    print ("Welcome to Marvel Rivals Role Randomizer!")
    print ("Enter the names of all players:")

    players = []
    for i in range(6):
        while True:
            name = input(f"Players {i+1}: ").strip()
            if name:
                players.append(name)
                break
            else:
                print("Please enter a valid name!")

    try:
        randomizer.add_players(players)

        while True:
            print(f"\nPlayers: {', '.join(players)}")
            print("\nOptions:")
            print("1. Randomize roles")
            print("2. Add new players")
            print("3. Quit")

            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == "1":
                assignment = randomizer.generate_role_assignment()
                randomizer.display_assignment(assignment)

               # Keep randomizing until user says no
                while True:
                    again = input("\nRandomize again? (y/n): ").strip().lower()
                    if again == 'y':
                        randomizer.play_sound() # Play sound effect
                        assignment = randomizer.generate_role_assignment()
                        randomizer.display_assignment(assignment)
                    else:
                        break

            elif choice == "2":
                print("\nEnter new player names:")
                new_players = []
                for i in range(6):
                    while True:
                        name = input(f"Player {i+1}: ").strip()
                        if name:
                            new_players.append(name)
                            break
                        else:
                            print("Please enter a valid name!")
                randomizer.add_players(new_players)
                players = new_players

            elif choice == "3":
                print("Thanks for playing!")
                break

            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

    except ValueError as e:
        print(f"Error: {e}" )

if  __name__ == "__main__":
    main()

