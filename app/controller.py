from app import app
from flask import render_template
from app.models.game import *
from app.models.player import *

@app.route('/list_players')
def index():
    return render_template("index.html", players= [player_1,player_2])

@app.route('/game_1')
def start_game():
    player_1 = Player("pepe", "rock")
    player_2 = Player("manoli", "scissors")

    result = playing_game(player_1, player_2)
    return render_template("index.html", game_result=result)

@app.route('/<p1_choice>/<p2_choice>')
def second_game(p1_choice, p2_choice):
    player_1 = Player("pepe", p1_choice)
    player_2 = Player("manoli", p2_choice)

    result = playing_game(player_1, player_2)
    return render_template("index.html", game_result=result)