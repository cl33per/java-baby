import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print ("{} of {}".format(self.value,self.suit))

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
            card.show()

# Suffle deck before assigning players 
deck = Deck()
deck.shuffle()

bob = Player("Bob")
bob.draw(deck)
bob.showHand()

jerry = Player("Jerry")
jerry.draw(deck)
jerry.showHand()

dave = Player("Dave")
dave.draw(deck)
dave.showHand()