from app import app
from flask import render_template
from app.models.game import player_1, player_2
from app.models.player import *

@app.route('/rock/scissors')
def index():
    return render_template("index.html", players=players)

@app.route('/playing_game')
def start_game():
    if player_1.choice == player_2.choice:
        return None
    elif player_1.choice == "scissors" and player_2.choice == "rock":
        return f"{player_2.name} wins"