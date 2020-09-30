print('-------------------------')
print("Let's play Py-Pac-Poe!")
print('-------------------------')
board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
winning_combos = [
    [0, 1, 2],
    [0, 4, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 4, 6],
    [2, 5, 8],
    [3, 4, 5],
    [6, 7, 8],
]
empty = '-'
player_x = 'X'
player_o = 'O'


def PrintBoard(board):
    print(" " + " " + " " + "|" + " " +
          " " + " " + "|" + " " + " ")
    print("-----------")
    print(" " + " " + " " + "|" + " " +
          " " + " " + "|" + " " + " ")
    print("-----------")
    print(" " + " " + " " + "|" + " " +
          " " + " " + "|" + " " + " ")


PrintBoard(board)


def init_board(n):
    board = {}
    for x in range(n):
        for y in range(n):
            board[(x, y)] = empty
    return board
