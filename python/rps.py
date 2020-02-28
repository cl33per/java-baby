from random import randint

playOptions = ["Rock", "Paper", "Scissors"]

#random select index betwee 0 and 2
computer = playOptions[randint(0,2)]

#Set player
player = False

while player == False:
    player = raw_input("Rock, Paper, Scissors?") #raw_input forces input as string
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
        else:
            print("You win",player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose",computer, "cut", player)
        else:
            print("You win", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win", player, "cut", computer)
    else:
        print("Not a valid play. Check your spelling")
    player = False #returns user back to false to restart game 
    computer = playOptions[randint(0,2)] #selects new index in array