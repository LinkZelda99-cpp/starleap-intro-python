# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
import string

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "shared/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.read()
    # wordlist: list of strings
    wordlist = line.split()
    # wordlist = string.split(line)
    print(f"{len(wordlist)} words loaded.")
    print('Enter play_hangman() to play a game of hangman!')
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word_count = len(words_dict)
    rand_index = randrange(0, word_count)
    word = words_dict[ rand_index ]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    pass # This tells your code to skip this function; delete it when you
         # start working on this function


def return_guessed():
    '''
    Returns the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    pass # This tells your code to skip this function; delete it when you
         # start working on this function

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######

    return None

play_hangman()