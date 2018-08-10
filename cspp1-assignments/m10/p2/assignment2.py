'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i in letters_guessed:
            return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    a_n = ""
    for i in secret_word:
        if i not in letters_guessed:
            a_n = a_n + "_"
        else:
            a_n = a_n + i
    return a_n

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str1 = ""
    a_n = string.ascii_lowercase
    for i in a_n:
        if i not in letters_guessed:
            str1 = str1+i
    return str1


def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    wrong_guess_count = 8
    entered_string_by_user = ""
    list1 = []
    while True:
        print("-----------")
        print("You have " +  str(wrong_guess_count) +" guesses left.")
        print("Available letters: " + get_available_letters(entered_string_by_user.split()))
        char_entered = input("Please guess a letter: ")
        entered_string_by_user = entered_string_by_user + " " + char_entered

        if char_entered not in list1:

            if is_word_guessed(secret_word, char_entered):
                print("Good guess: " + get_guessed_word(secret_word, entered_string_by_user.split()))

            else:
                print("Oops! That letter is not in my word: " + get_guessed_word\
                    (secret_word, entered_string_by_user.split()))
                wrong_guess_count -= 1
        else:
            print("the given letter is repeating:" + get_guessed_word\
                (secret_word, entered_string_by_user.split()))
        list1 = list1+entered_string_by_user.split()
        if get_guessed_word(secret_word, entered_string_by_user.split()) == secret_word:
            print("Congratulations, you won!")
            break
        elif wrong_guess_count == 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word)
            break



def main():
    '''
    Main function for the given program

    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secret_word = choose_word(wordlist).lower()
    hangman(secret_word)


if __name__ == "__main__":
    main()
