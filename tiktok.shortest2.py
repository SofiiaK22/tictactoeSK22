dictionary = {'x': [], 'o': []}
player = dictionary['x']
gameStatus = 0
board = ['_', '|', '_', '|', '_', '\n', '_', '|', '_', '|', '_', '\n', ' ', '|', ' ', '|', ' ']

def view():
        for d in dictionary['x']:
            board[d*2]= 'x'
        for d in dictionary['o']:
            board[d*2]= 'o'
        print(''.join(board))

view()

from wonlost import*

def isInputValid(conin, dictionary):
    if not conin.isdigit():
        return False
    n1 = int(conin)
    if n1 < 1 or  n1 > 9:
        return False
    c = n1-1
    for m in dictionary:
        if c in dictionary[m]:
            return False
    return True

#print(isInputn1alid('1', {'x': [1]}))

def inputCorrectDigit():
    conin = input()
    while not isInputValid(conin, dictionary): 
        print("Please enter a digit from 1 to 9:")
        conin = input()
    return int(conin)-1
   
while gameStatus == 0:
    n1 = inputCorrectDigit()
    player.append(n1)
    gameStatus = wonlost(player)
    if gameStatus == 0:
        player = dictionary['o'] if player is dictionary['x'] else dictionary['x']
    view()

if gameStatus == 1:
    print('Draw - Game over!')
elif gameStatus == 2:
    print( 'Player X won! - Game over!' if player is dictionary['x'] else 'Player O won! - Game over!')
