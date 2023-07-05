from Model.gameModel import GameModel

class GameView:
    def __init__(self):
        self.model = GameModel()

    def get_user_choice(self):
        valid_choices = ["rock", "paper", "scissors"]
        while True:
            choice = input("Enter your choice (rock/paper/scissors): ").lower()
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def display_result(self):
        result = self.model.get_result()
        print("Result: ", result)

    def run(self):
        print("Welcome to Rock Paper Scissors!")
        self.model.set_player_choice(self.get_user_choice())
        self.model.get_computer_choice()
        self.display_result()
