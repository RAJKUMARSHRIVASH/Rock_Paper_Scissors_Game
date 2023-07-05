from Controller.gameController import GameController

if __name__ == "__main__":
    controller = GameController()
    
    while True:
        controller.start()
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break