from app.models.player import *

def playing_game(player_1, player_2):
    while player_1.choice == player_2.choice:
        return "Nobody wins"

    if player_1.choice == "rock" and player_2.choice == "scissors":
        return f"{player_1.name} wins"
    elif player_1.choice == "rock" and player_2.choice == "paper":
        return f"{player_2.name} wins"
    elif player_1.choice == "paper" and player_2.choice == "scissors":
        return f"{player_2.name} wins"
    elif player_1.choice == "paper" and player_2.choice == "rock":
        return f"{player_1.name} wins"
    elif player_1.choice == "scissors" and player_2.choice == "paper":
        return f"{player_1.name} wins"
    elif player_1.choice == "scissors" and player_2.choice == "rock":
        return f"{player_2.name} wins"