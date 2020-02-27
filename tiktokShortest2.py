#!/usr/bin/python

dictionary = {'X': [], 'O': []}
player = 'X'
PC = 'O'
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
    return list(set(range(0,9)).difference(set(a)).difference(set(b)))
    
#print(freeSpaces(a, b), a, b)

def walk(a,b):
    temp = freeSpaces(a,b)
    if len(temp):
        result = random.choice(temp)
    return result 

#minimaxfun returns the list which the player uses to win depending in the variable player
def minimaxfun(minimax, player):    
    x = [-2,None] if player == 'O' else [2,None]
    for t in minimax:
        if player == 'O':
            if t[0] > x[0]:
                x = t
        elif player == 'X':
            if t[0] < x[0]:
                x = t
    #print('minimax:',minimax, player, x)
    return x
'''print(minimaxfun([[0,0], [-1,2]], 'X'))
exit(0)
minimax = [[0,0], [-1,2],[23,123]]
a = 0
for t in minimax:
    a += t[0]
print(x)
exit(0)
x = 2
for t in minimax:
    if t[0] < x:
        x = t[0]'''

def pathToTake(a,b,player):
    minimax = []
    if wonlost(a) == 2:
        return [-1, None]
    elif wonlost(a) == 1 or wonlost(b)==1:
        return [0, None]
    elif wonlost(b) == 2:
        return [1, None]
    else:                                                           
        nextPlayer = 'O' if player == 'X' else 'X'                 
        for x in freeSpaces(a,b):                                    
            newA = a.copy()
            newB = b.copy()
            if player == 'O':
                newB.append(x)
            else:
                newA.append(x)
            r = pathToTake(newA,newB, nextPlayer)
            t = [r[0], x]
            minimax.append(t)
    #if b==Listb and a==Lista:
    ##    print(minimax)
    #print('pathToTake:', a,b, player, minimax,freeSpaces(a,b))
    return minimaxfun(minimax, player)


def tryTheTry(a,b,player):
    if wonlost(dictionary[player]) == 0:
        thePath = pathToTake(a,b, player)
        #print(thePath)
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
