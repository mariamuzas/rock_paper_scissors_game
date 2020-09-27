from app.models.player import *

def playing_game(player_1, player_2):
    while player_1.choice == player_2.choice:
        return "Draw!!!"

    if player_1.choice == "rock" and player_2.choice == "scissors":
        return f"{player_1.name} wins!"
    elif player_1.choice == "rock" and player_2.choice == "paper":
        return f"{player_2.name} wins!"
    elif player_1.choice == "paper" and player_2.choice == "scissors":
        return f"{player_2.name} wins!"
    elif player_1.choice == "paper" and player_2.choice == "rock":
        return f"{player_1.name} wins!"
    elif player_1.choice == "scissors" and player_2.choice == "paper":
        return f"{player_1.name} wins!"
    elif player_1.choice == "scissors" and player_2.choice == "rock":
        return f"{player_2.name} wins!"
    elif player_1.choice == "fire" and player_2.choice == "paper":
        return f"Fire beats everything!"
    elif player_1.choice == "fire" and player_2.choice == "scissors":
        return f"Fire beats everything!"
    elif player_1.choice == "fire" and player_2.choice == "rock":
        return f"Fire beats everything!"
    elif player_1.choice == "fire" and player_2.choice == "water-balloon":
        return f"Well played, Pheobe Buffay!"
