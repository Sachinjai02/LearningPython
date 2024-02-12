from player import Player
from deck import Deck
from card import Card


class Game:

    def __init__(self):
        pass

    def play(self, CARDS_TO_BE_DRAWN_ON_WAR=5):
        game_on = True
        player1 = Player("Sachin")
        player2 = Player("Computer")
        deck = Deck()

        while len(deck.cards) > 0:
            player1.add_cards(deck.deal_one())
            player2.add_cards(deck.deal_one())

        round_num = 0
        while game_on:
            round_num += 1
            print(f'Round number : {round_num}')

            if len(player1.all_cards) == 0:
                print("Player1 is out of cards, Congratulations Player2")
                game_on = False
                break

            if len(player2.all_cards) == 0:
                print("Player2 is out of cards, Congratulations Player1")
                game_on = False
                break

            player1_cards = [player1.remove_one()]
            player2_cards = [player2.remove_one()]

            war_on = True

            while war_on:
                if player1_cards[0].value > player2_cards[0].value:
                    player1_cards.extend(player2_cards)
                    player1.add_cards(player1_cards)
                    war_on = False

                elif player2_cards[0].value > player1_cards[0].value:
                    player2_cards.extend(player1_cards)
                    player2.add_cards(player2_cards)
                    war_on = False

                else:
                    print("WAR!!!")
                    if len(player1.all_cards) < CARDS_TO_BE_DRAWN_ON_WAR:
                            game_on = False
                            print("Player 1 doesn't have enough cards. Congrats Player2!!")
                            break
                    elif len(player2.all_cards) < CARDS_TO_BE_DRAWN_ON_WAR:
                            game_on = False
                            print("Player 2 doesn't have enough cards. Congrats Player1!!")
                            break
                    else:
                        for card in range(CARDS_TO_BE_DRAWN_ON_WAR):
                            player1_cards.insert(0, player1.remove_one())
                            player2_cards.insert(0, player2.remove_one())


game = Game()
game.play(5)