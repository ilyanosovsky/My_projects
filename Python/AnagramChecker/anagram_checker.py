# What You Will Create
# 🌟 Anagram Checker
# We will create a program that will ask the user for a word.
# It will check if the word is a valid English word, and then find all possible anagrams for that word.

# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.
# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, 
# the function should return a list containing [“mate”, “tame”, “team”].)

class AnagramChecker :
    def __init__(self):
        with open("Week3/Day5/Anagram Checker/word_list.txt") as file:
            self.word_list = file.read().splitlines()

    def is_valid_word(self, word):
        return word in self.word_list

    def get_anagrams(self, word):
        anagrams = []
        for word_from_list in self.word_list:
            if sorted(word_from_list) == sorted(word):
                anagrams.append(word_from_list)
        return anagrams

# Hint: you might want to create a separate method called is_anagram(word1, word2), 
# that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)
    

    
