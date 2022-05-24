import random


class Puzzle:
    """The puzzle is a secret word randomly chosen from a list. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.

    Attributes: 
        _secret_word: string
    
    """


    def __init__(self):

        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._secret_words = []

    def create_words(self):
        """To create the words that will be used in the puzzle"""

        for i in range(5):
            self._secret_words.append(i)


    def random_select(self):
        """To randomly select a new word"""

        i = random.choice(self._secret_words)
        return i





