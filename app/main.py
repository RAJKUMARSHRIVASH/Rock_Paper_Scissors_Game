from flask import Flask, render_template, request, jsonify
from controllers.game_controller import GameController

app = Flask(__name__)
controller = GameController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choice = request.json['choice']
    controller.start_game(choice)
    result = controller.model.result
    return jsonify({'result': result})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
