# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.

from anagram_checker import AnagramChecker

anagram_checker = AnagramChecker()

def get_user_input():
    user_input = input("Please enter a word: ").upper().strip()
    return user_input

def validate_user_input(user_input):
    if len(user_input.split()) > 1:
        print("Please enter only one word")
        return False
    elif not user_input.isalpha():
        print("Please enter only alphabetic characters")
        return False
    else:
        return True
    
def print_anagrams(user_input):
    anagrams = anagram_checker.get_anagrams(user_input)
    print(f"Anagrams for your word: {', '.join(anagrams)}")

def print_validity(user_input):
    if anagram_checker.is_valid_word(user_input):
        print("This is a valid English word.")
    else:
        print("This is not a valid English word.")

def main():
    while True:
        user_input = get_user_input()
        if validate_user_input(user_input):
            print_validity(user_input)
            print_anagrams(user_input)
        else:
            continue
        if input("Would you like to enter another word? (Y/N): ").upper() == "Y":
            continue
        else:
            break
main()


