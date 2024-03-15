from card import Card


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1
