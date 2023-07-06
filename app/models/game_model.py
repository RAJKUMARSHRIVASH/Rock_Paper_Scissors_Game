import random

class GameModel:
    def __init__(self):
        self.player_choice = None
        self.computer_choice = None
        self.result = None

    def set_player_choice(self, choice):
        self.player_choice = choice

    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        self.computer_choice = random.choice(choices)

    def determine_result(self):
        if self.player_choice == self.computer_choice:
            self.result = "Tie"
        elif (
            (self.player_choice == "rock" and self.computer_choice == "scissors")
            or (self.player_choice == "paper" and self.computer_choice == "rock")
            or (self.player_choice == "scissors" and self.computer_choice == "paper")
        ):
            self.result = "You Win!"
        else:
            self.result = "You Lose!"
