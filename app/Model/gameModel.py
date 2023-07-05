class GameModel:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_choice = None
        self.computer_choice = None
        self.result = None

    def set_player_choice(self, choice):
        self.player_choice = choice

    def get_computer_choice(self):
        # Your logic to generate a random computer choice goes here
        # For now, let's just randomly select a choice from the list
        import random
        self.computer_choice = random.choice(self.choices)

    def get_result(self):
        if self.player_choice == self.computer_choice:
            self.result = "tie"
        elif (
            (self.player_choice == "rock" and self.computer_choice == "scissors")
            or (self.player_choice == "paper" and self.computer_choice == "rock")
            or (self.player_choice == "scissors" and self.computer_choice == "paper")
        ):
            self.result = "win"
        else:
            self.result = "lose"
        return self.result
