"""
Program Name: Word Count
Author: Xavier Chitison
Purpose: This program allows the user to select one of four text files.
         It reads the selected file, removes punctuation, converts words
         to lowercase, counts how many times each word appears, and
         displays the results in alphabetical order.
Starter Code: No starter code was used.
Date: September 26, 2026
"""
from pathlib import Path
import string


class WordAnalyzer:
    """Reads a text file and counts how often each word appears."""

    def __init__(self, filepath):
        # Store the filepath as a private Path object
        self.__filepath = Path(filepath)

        # Private dictionary for word frequencies
        self.__frequencies = {}
    def process_file(self):
        """Read the file and count each word."""

        try:
            # Check if the file exists
            if not self.__filepath.exists():
                raise FileNotFoundError

            # Create a translation table that removes punctuation
            translator = str.maketrans("", "", string.punctuation)

            # Open and read the file line by line
            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:

                    # Convert to lowercase
                    line = line.lower()

                    # Remove punctuation
                    line = line.translate(translator)

                    # Split the line into individual words
                    words = line.split()

                    # Count each word
                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True
        except FileNotFoundError:
            print(f"\nError: '{self.__filepath.name}' was not found.")
            return False

    def print_report(self):
        """Print all words and their counts alphabetically."""

        # Get and sort the dictionary keys
        words = sorted(self.__frequencies.keys())

        print("\n--- Word Count Report ---")

        for word in words:
            print(f"{word:<20} :: {self.__frequencies[word]}")


def main():
    """Main driver for the Word Analyzer program."""

    # Get the folder where this Python program is located
    project_folder = Path(__file__).parent

    # Dictionary containing the four text file paths
    files = {
        "1": project_folder / "Tarzan.txt",
        "2": project_folder / "treasure_island.txt",
        "3": project_folder / "monte_cristo.txt",
        "4": project_folder / "princess_mars.txt"
    }

    # Names displayed in the menu
    display_names = {
        "1": "Tarzan",
        "2": "Treasure Island",
        "3": "The Count of Monte Cristo",
        "4": "A Princess of Mars"
    }