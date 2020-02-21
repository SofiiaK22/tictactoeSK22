from judge import *
from view import *


PlayerXTurns = []
Player0Turns = []
gameOver = 0
activePlayer = PlayerXTurns

def checkInput(conin):
    result = 0
    if(conin.isdigit()) and (int(conin) > 0 and int(conin) < 10) and (int(conin) not in PlayerXTurns and int(conin) not in Player0Turns):
        result = 1
    else:
        print('Please make a correct input')
    return result


while 0 == gameOver:
    conin = input() 
    if not checkInput(conin):
        continue

    activePlayer.append(int(conin)-1)
    gameOver = judge(activePlayer)
    activePlayer = Player0Turns if activePlayer is PlayerXTurns else PlayerXTurns
    redraw(Player0Turns,PlayerXTurns)
    
if 1 == gameOver:
    print('Draw - Game over!')
else:
    print( 'Player X won! - Game over!' if activePlayer is PlayerXTurns else 'Player 0 won! - Game over!')
