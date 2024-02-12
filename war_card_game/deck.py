import random
import card


class Deck:

    def __init__(self):
        self.cards = self.create_cards()
        random.shuffle(self.cards)

    def create_cards(self):
        cards = []
        for suite in card.card_suites:
            for rank in card.card_ranks:
                cards.append(card.Card(suite, rank))
        return cards

    def deal_one(self):
        return self.cards.pop()


deck = Deck()
for cards in range(1, 53):
    print(deck.deal_one())
