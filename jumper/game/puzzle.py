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
        self._secret_word = []

