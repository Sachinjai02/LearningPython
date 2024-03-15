from card import card_suites
from card import card_values
from card import Card
from random import shuffle


class Deck():

    def __init__(self):
        self.deck = []
        for suit in card_suites:
            for card_val in card_values:
                self.deck.append(Card(suit, card_val))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return f"Deck has: {deck_comp}"

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
