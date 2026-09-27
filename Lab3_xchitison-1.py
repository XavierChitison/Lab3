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
            return False

        except FileNotFoundError:
            print(f"\nError: '{self.__filepath.name}' was not found.")
            return False