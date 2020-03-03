import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self,name):
        print ("{} has {} of {}".format(name, self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in["Spades","Clubs","Hearts","Diamonds"]:
            for v in ["2","3","4","5","6","7","8","9","J","Q","K","A"]:
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show(self.name)
class Game:
    deck = Deck()
    deck.shuffle()

    def playGame(self):
        numberOfPlayers = int(input("Number of Players?: "))
        playersCounter = 0
        playerList = []

        while playersCounter < numberOfPlayers:
            name = raw_input("Enter Player Name: ")
            playerList.append(Player(name))
            playersCounter = playersCounter + 1 
            
        for players in playerList:
            players.draw(self.deck) 
            players.showHand()
            # print (playerList[players])

        # for players in range(len(playerList)):
        #     print (playerList[players])
        

    def compareCards(self):
        a = [1, 2, 3, 4, 5] 
        for x in range(len(a)):
            print (a[x],) 

# Suffle deck before assigning players 
game = Game()
game.playGame()
# game.compareCards()