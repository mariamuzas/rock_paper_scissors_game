from app.models.player import *

player_1 = Player("pepe", "rock")
player_2 = Player("manoli", "scissors")

class Game:
    def playing_game(self, player_1, player_2):

        if player_1.choice == "rock" and player_2.choice == "scissors":
            return f"{player_2.name} wins"
        elif player_1.choice == player_2.choice:
            return "yes"




# def start_game(choice_1, choice_2):
#     player_1 = Player("Pepe", choice)
#     player_2 = Player("Manoli", choice)

#     if choice_1 == choice_2:
#         return None
#     elif choice_1 == "scissors" and choice_2 == "rock":
#         return f"{player_2.name} wins"
