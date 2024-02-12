class Card():
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self):
        return f"Card is {self.rank} of {self.suite}"

card_suites = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
card_values = {'Ace' : 14, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
               'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13}
card_ranks = card_values.keys()
