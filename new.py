dictionary = {'X': [], 'O': []}
player = 'X'
gameStatus = 0
board = ['_', '|', '_', '|', '_', '\n', '_', '|', '_', '|', '_', '\n', ' ', '|', ' ', '|', ' ']

def view():
    print(dictionary)
    for d in dictionary['X']:
        board[d*2]= 'X'
    for d in dictionary['O']:
        board[d*2]= 'O'
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

#print(isInputn1alid('1', {'X': [1]}))

def inputCorrectDigit():
    conin = input()
    while not isInputValid(conin, dictionary): 
        print("Please enter a digit from 1 to 9:")
        conin = input()
    return int(conin)-1
   
while gameStatus == 0:
    n1 = inputCorrectDigit()
    dictionary[player].append(n1)
    gameStatus = wonlost(dictionary[player])
    if gameStatus == 0:
        player = 'O' if player is 'X' else 'X'
    view()

if gameStatus == 1:
    print('Draw - Game over!')
elif gameStatus == 2:
    print( 'Player ', player, ' won! - Game over!')