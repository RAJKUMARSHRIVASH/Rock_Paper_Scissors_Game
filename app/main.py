from flask import Flask, render_template, request, jsonify

from Controller.gameController import GameController

# if __name__ == "__main__":
#     controller = GameController()
    
#     while True:
#         controller.start()
        
#         play_again = input("Do you want to play again? (y/n): ").lower()
#         if play_again != 'y':
#             break


app = Flask(__name__)
controller = GameController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choice = request.json['choice']
    controller.model.set_player_choice(choice)
    controller.start()
    result = controller.view.model.result
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
