import random


def is_valid_input(letter_guessed, old_letters_guessed):
    """
    is_valid_input gets input from the user.
    The function checks if the input have only one letter and if the letter is alpha
    (letter and not & *%$ and so on),
    :param letter_guessed: A letter that the function gets from the user,
    :type: str,
    :return: True if the letter is valid. else False,
    """
    if len(letter_guessed) > 1 and letter_guessed.isalpha() is not True:
        return False

    elif letter_guessed.isalpha() is not True:
        return False

    elif len(letter_guessed) > 1:
        return False

    elif letter_guessed in old_letters_guessed:
        return False

    else:
        guessed_letters.append(letter_guessed)
        return True


def print_string(my_str):
    """
    the function will convert list to string to print it
    :param my_str: word you should guess
    :return: list to string
    """
    my_str = "".join(my_str)
    return my_str


def max_checker(max_lives):
    """
    The function checks how many lives you have every time you
    enter a letter
    :param max_lives: checks how many lives you have.
    :type: int
    :return: the index of HANGMANPICS
    """
    if max_lives == 6:
        return 0
    elif max_lives == 5:
        return 1
    elif max_lives == 4:
        return 2
    elif max_lives == 3:
        return 3
    elif max_lives == 2:
        return 4
    elif max_lives == 1:
        return 5
    elif max_lives == 0:
        return 6


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
WORDS = ("abandon", "ability", "especially", "language",
         "knowledge", "killing", "Israeli", "interested",
         "household", "grocery", "potential", "presidential",
         "population", "gradually", 'actual', "additional", "attitude", "book", "bullet")

word = random.choice(WORDS).lower()
censor_word = "_" * len(word)
censor_word = list(censor_word)
guessed_letters = []
MAX_TRIES = 6
is_word_correct = False
HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""


print("Welcome to the game Hangman")

print(f"{HANGMAN_ASCII_ART}\nmax tries: {MAX_TRIES}")

print(print_string(censor_word))
while MAX_TRIES > 0 and is_word_correct is not True:

    guess_letter = input("\nGuess a letter: ").lower()

    is_letter_there = False

    if is_valid_input(guess_letter, guessed_letters):
        for i in range(len(word)):

            if guess_letter == word[i]:

                censor_word[i] = guess_letter
                is_letter_there = True

        if is_letter_there is False:

            MAX_TRIES -= 1
            print(f"{HANGMANPICS[max_checker(MAX_TRIES)]}\nMax tries: {MAX_TRIES}\n{print_string(censor_word)}")
        else:

            print(f"{HANGMANPICS[max_checker(MAX_TRIES)]}\nMax tries: {MAX_TRIES}\n{print_string(censor_word)}")
        if print_string(censor_word) == word:

            is_word_correct = True
    elif guess_letter in guessed_letters:
        print("You entered this char earlier!")
    else:
        print("ERROR! pls enter valid letter!")
else:
    if is_word_correct is True:
        print(f"Wow awesome! You did it! you find the correct word:\n{print_string(censor_word)}")
    else:
        print("Sorry you lost the game... Try next time")