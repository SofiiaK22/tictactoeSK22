from judge import *
from view import *
dictionary = {'x': [], 'o': []}
gameStatus = 0
Player = dictionary['x']

def checkInput(conin):
    result = 0
    if(conin.isdigit()) and (int(conin) > 0 and int(conin) < 10) and (int(conin) not in dictionary['x'] and int(conin) not in dictionary['o']):
        result = 1
    else:
        print('Please make a correct input')
    return result


while gameStatus == 0:
    conin = input() 
    if not checkInput(conin):
        continue
    Player.append(int(conin)-1)
    gameStatus = wonlost(Player)
    Player = dictionary['o'] if Player is dictionary['x'] else dictionary['x']
    redraw(dictionary['x'],dictionary['o'])
    
if gameStatus == 1:
    print('Draw - Game over!')
elif gameStatus == 2:
    print( 'Player X won! - Game over!' if activePlayer is dictionary['x'] else 'Player 0 won! - Game over!')
