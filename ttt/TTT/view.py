import os
board = ['_', '|', '_', '|', '_', '\n', '_', '|', '_', '|', '_', '\n', ' ', '|', ' ', '|', ' ']

def redraw(a, b):
    os.system("cls")
    for d in a:
        board[d*2]= 'X'
    for d in b:
        board[d*2]= 'O'
    print(''.join(board))
