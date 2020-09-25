from app import app
from flask import render_template
from app.models.game import *
from app.models.player import *

# @app.route('/rock/scissors')
# def index():
#     return render_template("index.html", players= [player_1,player_2])

@app.route('/game_2')
def start_game():
    game = Game()
    result = game.playing_game(player_1, player_2)
    return render_template("index.html", game_result=result)


    # result = Game.play(player_1, player_2)

# def start_game(choice_1, choice_2):
#     if choice_1 == choice_2:
#         return None
#     elif choice_1 == "scissors" and choice_2 == "rock":
#         return f"{player_2.name} wins"