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

def pathToTake(a,b,player):
    if wonlost(a) == 2:
        u = [+1, None]
    if wonlost(a) == 1 or wonlost(b)==1:
        u = [0, None]
    if wonlost(b) == 2:
        u = [-1, None]
    nextPlayer = 'O' if player == 'X' else 'X'
    theTryb = b.copy()
    theTrya = a.copy()
    for x in freeSpaces(theTrya,theTryb):   
        if player == 'O':
            theTryb.append(x)
        else:
            theTrya.append(x)
        pathToTake(theTrya,theTryb, nextPlayer)
        return x
    useableList = [u[0], x]
    return useableList


def tryTheTry(a,b,player):
    if wonlost(dictionary[player]) == 0:
        thePath = pathToTake(a,b, player)
    return int(thePath[1])    
'''    else:
        thePath = '''

def inputCorrectDigit(conin):
    while not isInputValid(conin, dictionary): 
        print("Please enter a digit from 1 to 9:")
        conin = input()
    return int(conin)-1
'''   
while gameStatus == 0:
    n1 = inputCorrectDigit()
    onlost() == 2:
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
        n1 = tryTheTry(a, b, player)
        dictionary[player].append(n1)
    gameStatus = wonlost(dictionary[player])
    if gameStatus == 0:
        player = 'O' if player == 'X' else 'X'
    view()

if gameStatus == 1:
    print('Draw - Game over!')
elif gameStatus == 2:
    print( 'Player ', player, ' won! - Game over!')
