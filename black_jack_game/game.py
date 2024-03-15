from card import Card
from deck import Deck
from hand import Hand
from chip import Chips

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def take_hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Hit or Stand? Enter h or s ")
        if x[0].lower() == 'h':
            take_hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's turn")
            playing = False
        else:
            print("Sorry, I did not understand that, Please enter h or s!")
            continue
        break


def show_some(player, dealer):
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    for card in dealer.cards[1:]:
        print(card)
    print("\n Player's Hand:")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("\n Dealer's Hand: ", *dealer.cards, sep="\n")
    print(f"Value of Dealer's hand is: {dealer.value}")

    print("\n Player's Hand: ", *player.cards, sep="\n")
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("BUST DEALER")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! PUSH")


while True:
    print("Welcome to black jack game!")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            take_hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print("\n Player total chips are: {}".format(player_chips.total))

    new_game = input("Do you wish to play again ? (press y to yes)")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    print("Thank you for playing!")
    break
