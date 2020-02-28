from random import randint

dieSides = [1,2,3,4,5,6]

def rolldice(dieSides):
    diceroll = dieSides[randint(0,5)]
    return diceroll

print rolldice(dieSides)