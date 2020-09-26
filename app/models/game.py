from app.models.player import *

def playing_game(player_1, player_2):
    if player_1.choice == "rock" and player_2.choice == "scissors":
        return f"{player_2.name} wins"
    elif player_1.choice == player_2.choice:
        return "draw"
