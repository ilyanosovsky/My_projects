# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
word = word.upper()
word_letters = set(word)
alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
used_letters = set()

lives = 6

hangman_pics = [
    """
       +---+
           |
           |
           |
          ===
    """,
    """
       +---+
       O   |
           |
           |
          ===
    """,
    """
       +---+
       O   |
       |   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
      /    |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
      / \  |
          ===
    """
]

def display_hangman(lives):
    print(hangman_pics[lives])


while len(word_letters) > 0 and lives > 0:

    print(f"You have {lives} lives left and you have used these letters: {' '.join(used_letters)}")

    word_list = [letter if letter in used_letters else '*' for letter in word]
    print('Current word: ', ' '.join(word_list))

    display_hangman(lives)
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives -= 1
            print('Letter is not in word.')
    elif user_letter in used_letters:
        print('You have already used that letter. Please try again.')
    else:
        print('Invalid character. Please try again.')

if lives == 0:
    print('You died, sorry. The word was', word)
else:
    print('You guessed the word', word, '!!')


