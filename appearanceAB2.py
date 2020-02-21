board = ['_', '|', '_', '|', '_', '\n', '_', '|', '_', '|', '_', '\n', ' ', '|', ' ', '|', ' ']
def view(dictionary['x'], dictionary['o']):
        for d in dictionary['x']:
            board[d*2]= 'x'
        for d in dictionary['o']:
            board[d*2]= 'o'
        print(''.join(board))
