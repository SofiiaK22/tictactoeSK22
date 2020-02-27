#!/usr/bin/python

dictionary = {'X': [1,6, 8], 'O': [3, 5, 7]}
player = 'X'
Lista = dictionary['X']
Listb = dictionary['O']
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
    return list(set(range(0,9)).difference(set(Lista)).difference(set(Listb)))
    
#print(freeSpaces(a, b), a, b)

def walk(a,b):
    temp = freeSpaces(a,b)
    if len(temp):
        result = random.choice(temp)
    return result 

def pathToTake(a,b,player,u, f):
    useableList = [0]
    minimax = []
    print(a,b, player)
    if wonlost(a) == 2:
        u = -1
    elif wonlost(a) == 1 or wonlost(b)==1:
        u = 0
    elif wonlost(b) == 2:
        u = +1
    else:                                                           #I shouldn't have copied the a and b
        nextPlayer = 'O' if player == 'X' else 'X'                  #player change, it's correct
        newA = a.copy()
        newB = b.copy()
        for x in freeSpaces(a,b):                                    #so it uses the right x and the correct freeSpaces(), and it is also just moving "horizontaly"(talking about the table), not downwards
            useableList.append(x)
            print('x=',x)
            #if player == 'O':
            #    newB.append(x)
            #else:
            #    newA.append(x)
            r = pathToTake(newA,newB, nextPlayer,u, f)
            print(r)
            minimax.append(r)
        for t in minimax:
            if player == 'O' and t[0] == 1:
                u = t[1]
                f = t[2]
                newB.append(t[1])
            elif player == 'x' and t[0] == -1:
                u = t[1]
                f = t[2]
                newA.append(t[1])
            elif t[0] == 0:
                u = t[1]
                f = t[2]
                if player == 'O':
                    newB.append(f)
                else:
                    newA.append(f)
        useableList[0] = u
    return useableList


def tryTheTry(a,b,player):
    if wonlost(dictionary[player]) == 0:
        thePath = pathToTake(a,b, player, None, None)
        print(thePath)
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
        n1 = tryTheTry(Lista, Listb, player)
        dictionary[player].append(n1)
    gameStatus = wonlost(dictionary[player])
    if gameStatus == 0:
        player = 'O' if player == 'X' else 'X'
    view()

if gameStatus == 1:
    print('Draw - Game over!')
elif gameStatus == 2:
    print( 'Player ', player, ' won! - Game over!')
