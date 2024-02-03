from random import shuffle


def shuffle_list(list):
    shuffle(list)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0, 1 or 2: ")
    return int(guess)


def check_guess(list, guess):
    if list[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(list)


cups = [' ', ' ', 'O']
shuffle_list(cups)
guess = player_guess()
check_guess(2, guess)
