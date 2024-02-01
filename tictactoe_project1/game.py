def print_board(board):
    length = len(board)
    for r in range(0, length):
        print('| ', end='')
        for c in range(0, length):
            print(board[r][c]+ " ", end='')
        print('|')

def get_user_choice(row_column, range_low, range_high):
    r = ' '
    while not r.isdigit() or (r.isdigit() and not int(r) in range(range_low,range_high+1)):
        r = input(f"Enter {row_column} ")
        if not r.isdigit() or (r.isdigit() and not int(r) in range(range_low,range_high+1)):
            print("Sorry wrong input, please try again!")
    return int(r)

def create_board(size):
    board = []
    for i in range (0, size):
        col = []
        for j in range (0, size):
            col.append('-')
        board.append(col)
    return board

def check_win_draw(board, player):
    game_status = True
    filled = 0
    size = len(board)
    for r in range(0, size):
        for c in range (0, size):
            if board[r][c] != '-':
                filled = filled+1

    if filled != size ** 2:
        print("The game results in a draw!")
        return False

    ## Check for horizontal wins

    ## check for diagonal wins
    ## check for vertical wins

    return True

def game():
    game_status = True
    size = get_user_choice("Tic tac toe board size (1-10)", 1, 10)
    board = create_board(size)
    print_board(board)
    print("Player one ------- X")
    print("Player two --------0")
    print("Player one to begin....")
    players = [("Player1 [X]",'X'), ("Player2 [0]",'0')]
    player_turn = 0
    while game_status:
        print(f" {players[player_turn][0]}, please make a choice")
        row = get_user_choice(f"Row index(0-{size-1})",0, size-1)
        col = get_user_choice(f"Col index(0-{size-1})",0, size-1)
        if board[row][col] != '-':
            print("Invalid indices, this selection is already made. Please try again")
            continue
        board[row][col] = players[player_turn][1]
        print_board(board)


        game_status = check_win_draw(board,players[player_turn][0])

        player_turn = (player_turn + 1) % 2


game()