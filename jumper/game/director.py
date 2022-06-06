from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.man import Man

"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _is_playing (boolean): Whether or not to keep playing.
        _puzzle: holding the puzzle
        _secret_word: selecting the secret word
        _man: holding the man 
        _terminal_service: For getting and displaying information on the terminal.
        

    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._puzzle = Puzzle()
        self._secret_word = self._puzzle.get_word()
        self._man = Man(self._secret_word)
        self._terminal_service = TerminalService()


    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """The game starts by guessing a letter

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text("")
        for letter in self._man.get_blank_puzzle():
            self._terminal_service.write_text(letter, end= " ")

        self._terminal_service.write_text("")
        self._terminal_service.write_text(self._man.parachute()) #shows the parachute
        
        self._terminal_service.write_text("") #add newline that is blank
        self._user_letter= self._terminal_service.validateInput("Guess a letter [a-z]: ", "[a-z]") #gets user's letter 
        self._terminal_service.write_text(f"your input: {self._user_letter}") #displays the user's letter

    def _do_updates(self):
        """It updates the letter guess against the letter that should be guess
        
        Args:
            self (Director): An instance of Director.
        """
        self._man.check_guess(self._user_letter)

    def _do_outputs(self):
        """Every wrong guess, the parachute is beginning to fall

        Args:
            self (Director): An instance of Director.
        """
        print(self._man.parachute())
        continuing = self._man.fails #checks the fail count
        print(continuing,'wrong guess!!')
        if continuing == 5:
             self._is_playing = False
             print('Im sorry!!!')
             return self._is_playing
         
        else:
            
            if self._secret_word == self._man._winning_word:
                print('You did it! Congratulations YOU WIN!!!')
                self._is_playing = False
                return self._is_playing
            else:   
                
                self._is_playing = True
                print('try it again!!!',)
                return self._is_playing
