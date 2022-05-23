# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

# Cnsts
HANGMAN = ['''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = ["BEAR", "PIZZA", "SNAKE", "WASHINGTON", "MOON"]

MAX_WRONG = len(HANGMAN) - 1


# Initialize Variables
def rungame():
    # Pick a word
    word = random.choice(WORDS)

    # Dashes for each letter in a word
    current_guess = "-" * len(word)

    # print(word)
    # print(current_guess)

    # Wrong Guess Counter
    wrong_guesses = 0

    # Used Letters Tracker
    used_letters = []

    # Main Loop
    print("Welcome to hangmann")
    print("Try to Guess the Word")

    while wrong_guesses < MAX_WRONG and current_guess != word:
        print(HANGMAN[wrong_guesses])
        print("You have used the following letters: ", used_letters)
        print("So far, the word is: ", current_guess)

        guess = input("Enter your letter guess:")
        guess = guess.upper()

        # check if letter was already used
        while guess in used_letters:
            print("You have already guessed that letter", guess)
            guess = input("Enter your letter guess:")
            guess = guess.upper()

        # Add new guessed letter to list of guessed letters
        used_letters.append(guess)

        # Check guess
        if guess in word:
            print("You have guessed correctly!")

            # Give a new version of the word with mixed letters and dashes

            new_current_guess = ""
            for letter in range(len(word)):
                if guess == word[letter]:
                    new_current_guess += guess
                else:
                    new_current_guess += current_guess[letter]

            current_guess = new_current_guess
            # print(new_current_guess)

        else:
            print("Sorry that was incorrect")
            # Increase the number of incorrect by 1
            wrong_guesses += 1

    # End the game
    if wrong_guesses == MAX_WRONG:
        print(HANGMAN[wrong_guesses])
        print("HUNG!")
        print("The correct word is", word)

    else:
        print("You have won!")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    a = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rungame()
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
