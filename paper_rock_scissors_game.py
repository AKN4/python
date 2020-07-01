# two-player Rock-Paper-Scissors game

giris=("ROCK, PAPER, SCISSORS GAME")

print(giris)

first_player=input ("1. player ... Rock or Paper or Scissors?")
second_player=input ("2. player ... Rock or Paper or Scissors?")
if first_player==second_player:
    print ("Please again...")
else:
    if first_player=="Rock" and second_player=="Paper":
        print("2.Player win,  congratulations!!!")
    elif first_player=="Rock" and second_player=="Scissors":
        print("1.Player win,  congratulations!!!")
    elif first_player=="Paper" and second_player=="Scissors":
        print("2.Player win,  congratulations!!!")
    elif first_player=="Paper" and second_player=="Rock":
        print("1.Player win,  congratulations!!!")
    elif first_player=="Scissors" and second_player=="Rock":
        print("2.Player win,  congratulations!!!")
    else:
        print("1.Player win,  congratulations!!!")