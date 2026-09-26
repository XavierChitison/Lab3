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