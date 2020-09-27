from app import app
from flask import render_template
from app.models.game import *
from app.models.player import *

@app.route('/list_players')
def index():
    player_1 = Player("Pepe", "rock")
    player_2 = Player("Manoli", "scissors")
    return render_template("index.html", players= [player_1,player_2])

@app.route('/game_1')
def start_game():
    player_1 = Player("Pepe", "rock")
    player_2 = Player("Manoli", "scissors")
    result = playing_game(player_1, player_2)
    return render_template("index.html", game_result=result)

@app.route('/<p1_choice>/<p2_choice>')
def second_game(p1_choice, p2_choice):
    player_1 = Player("Pepe", p1_choice)
    player_2 = Player("Manoli", p2_choice)

    result = playing_game(player_1, player_2)
    return render_template("index.html", second_game_result=result)

@app.route('/how_to_play/')
def intruccions():
    return render_template("how_play.html")