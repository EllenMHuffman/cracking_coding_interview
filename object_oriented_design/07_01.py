# Deck of Cards: Design the data structures for a generic deck of cards. Explain
# how you would subclass the data structures to implement blackjack.
import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):

        return '<Card {} of {}s>'.format(self.value, self.suit)


class Deck:

    def __init__(self):
        self.cards = []

        suits = ['heart', 'spade', 'diamond', 'club']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        num_of_cards = len(self.cards)

        for _ in range(100):
            a = random.randint(0, num_of_cards - 1)
            b = random.randint(0, num_of_cards - 1)

            self.cards[a], self.cards[b] = self.cards[b], self.cards[a]


class BlackJack:

    def __init__(self):
        self.deck = Deck()
        self.player_1 = []
        self.player_2 = []
        self.player_3 = []
        self.house = []

    def deal_cards(self, rounds):
        """Deal one card to each player for specified number of rounds."""

        self.deck.shuffle()

        for _ in range(rounds):
            self.player_1.append(self.deck.cards.pop())
            self.player_2.append(self.deck.cards.pop())
            self.player_3.append(self.deck.cards.pop())
            self.house.append(self.deck.cards.pop())

    def hit(self, player):
        card = self.deck.cards.pop()
# NEED TO CREATE A PLAYER CLASS THAT CAN MAKE NEW PLAYER OBJECTS WITH THEIR OWN HANDS

        return card