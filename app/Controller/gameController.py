from View.gameView import GameView

class GameController:
    def __init__(self):
        self.view = GameView()

    def start(self):
        self.view.run()

if __name__ == "__main__":
    controller = GameController()
    controller.start()
