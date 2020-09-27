from app import app
from flask import render_template
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    player_1 = Player("Joey", "rock")
    player_2 = Player("Pheobe", "scissors")
    return render_template("how_play.html", players= [player_1,player_2])

@app.route('/game_1_test')
def start_game():
    player_1 = Player("Joey", "rock")
    player_2 = Player("Pheobe", "scissors")
    result = playing_game(player_1, player_2)
    return render_template("index.html", game_result=result)

@app.route('/<p1_choice>/<p2_choice>')
def the_game(p1_choice, p2_choice):
    player_1 = Player("Joey", p1_choice)
    player_2 = Player("Pheobe", p2_choice)

    result = playing_game(player_1, player_2)
    return render_template("index.html", the_game_result=result)

@app.route('/')
def instructions():
    return render_template("how_play.html")
