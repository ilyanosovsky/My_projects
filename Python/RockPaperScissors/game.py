# Steps
# Part I - Game.Py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. 
# Return the item at the end of the function.



class Game:
    def __init__(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        # self.result = {}

    @staticmethod
    def get_user_item():
            user_item = input("Please select an item: \n'R' for rock \n'P' for paper \n'S' for scissors: \n").upper()
            while user_item not in ["R", "P", "S"]:
                user_item = input("Try again. Please select a valid item: \n'R' for rock \n'P' for paper \n'S' for scissors: \n").upper()
            return user_item

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. 
# Return the item at the end of the function. Use python’s random.choice() function (read about it online).
    @staticmethod
    def get_computer_item():
        import random
        computer_item = random.choice(["R", "P", "S"])
        return computer_item
    
# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, 
# draw means the user and the computer got the same item, and loss means that the user has lost.

    def get_game_result(self):
        if self.user_item == self.computer_item:
            return "draw"
        elif (self.user_item == "R" and self.computer_item == "S") or (self.user_item == "P" and self.computer_item == "R") or (self.user_item == "S" and self.computer_item == "P"):

            return "win"
        else:
            return "loss"
        
# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. 
# You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, 
# draw means the user and the computer got the same item, and loss means that the user has lost.

    def play(self):
        print(f"You selected {self.user_item}. The computer selected {self.computer_item}. You {self.get_game_result()}.")
        return self.get_game_result()