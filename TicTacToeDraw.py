# https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

game_board = [
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
]


def update_game_board(move):
    for i, board in enumerate(game_board):
        if str(board[move[1] - 1]) not in ("XY") and i == move[0] - 1:
            board[move[1] - 1] = "X"
            break
        elif i == move[0] - 1:
            print("This move cant be done!")
            break


def get_move():
    while True:
        move = input("> ").split(",")
        if len(move) == 2:
            if move[0] in ("123") and move[1] in ("123"):
                return move


while True:
    print(game_board)
    for board in game_board:
        if 0 in board or 1 in board:
            break
    else:
        print("The game has ended!")
        break
    print("Please enter a move in row and column order!!! ")
    ft_move = [int(i) for i in get_move()]
    print(ft_move)
    update_game_board(ft_move)
