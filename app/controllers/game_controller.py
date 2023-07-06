from models.game_model import GameModel

class GameController:
    def __init__(self):
        self.model = GameModel()

    def start_game(self, choice):
        self.model.set_player_choice(choice)
        self.model.get_computer_choice()
        self.model.determine_result()
