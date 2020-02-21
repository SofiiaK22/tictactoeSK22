#!/usr/bin/python

dictionary = {'X': [], 'O': []}
player = 'X'
a = dictionary['X']
b = dictionary['O']
gameStatus = 0

import random

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

    
def gameEnding(gameStatus):
    if gameStatus == 1:
        print('Draw - Game over!')
    elif gameStatus == 2:
        print( 'Player ', player, ' won! - Game over!')
 

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

def freeSpaces(a,b):
    return list(set(range(0,9)).difference(set(a)).difference(set(b)))
    
#print(freeSpaces(a, b), a, b)

def walk(a,b):
    temp = freeSpaces(a,b)
    if len(temp):
        result = random.choice(temp)
    return result 

def pathToTake(player): 
    temp = freeSpaces(a,b)
    theTry = dictionary[player].copy()
    for x in temp:
        theTry.append(x)
        gameStatus = wonlost(theTry)
        gameEnding(gameStatus)
        player = 'O' if player == 'X' else 'X'
        if wonlost(theTry) == 2:
            result = int(x)        
            break
        elif wonlost(theTry) == 1:
            result = int(x)
            break
        elif wonlost(player) == 2:
            result = int(x)
            break
        player = 'O' if player == 'X' else 'X'
        pathToTake(player)
        theTry.remove(x)
        return result


def tryTheTry():
    if wonlost(dictionary[player]) != 0:
        pathToTake('O')

def inputCorrectDigit(conin):
    while not isInputValid(conin, dictionary): 
        print("Please enter a digit from 1 to 9:")
        conin = input()
    return int(conin)-1
'''   
while gameStatus == 0:
    n1 = inputCorrectDigit()
    dictionary[player].append(n1)
    gameStatus = wonlost(dictionary[player])
    if gameStatus == 0:
        player = 'O' if player == 'X' else 'X'
    view()
'''
#print(freeSpaces(a, b))


while gameStatus == 0:
    if player == 'X':
        n1 = inputCorrectDigit(input())
        dictionary[player].append(n1)
    else: 
        n1 = tryTheTry()
        dictionary[player].append(n1)
    gameStatus = wonlost(dictionary[player])
    gameEnding(gameStatus)
    if gameStatus == 0:
        player = 'O' if player == 'X' else 'X'
    view()

