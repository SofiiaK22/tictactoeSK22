# i - horz f/3
# j - vert f%3
import random
def wonlost(turnsList):
    result = 0
    if len(turnsList) >= 3:
        if checkWin(turnsList) == 2:
            result = 2
        elif 5 == len(turnsList):
            result = 1
    return result

def checkWin(turnsList):
    result = 0
    checks = [checkDiagonalForward, checkDiagonalBackward, checkHorisontal, checkVertical]
    if max([check(turnsList) for check in checks]) == 3:
        result = 2        
    return result


def checkDiagonalForward(turnsList):
    result = 0
    for f in turnsList:
        if f//3 == f%3:
            result+=1
    return result
    
def checkDiagonalBackward(turnsList):
    result = 0
    for f in turnsList:
        if 3-(f//3)-1 == f%3:
            result+=1
    return result
    
def checkHorisontal(turnsList):
    result = 0
    listI = [0,0,0]
    for f in turnsList:
        listI[f//3] += 1
    return max(listI)
    
def checkVertical(turnsList):
    result = 0
    listJ = [0,0,0]
    for f in turnsList:
        listJ[f%3] += 1
    return max(listJ)
'''
def freeSpaces(a,b):
    #space = [0,1,2,3,4,5,6,7,8]
    #set_space = set([0,1,2,3,4,5,6,7,8])
    #listWithoutX=[x for x in space if x not in a]
    #freeSpace=[x for x in listWithoutX if x not in b]
    #set_a = set(a)
    #set_b = set(b)
    
    
    
    #result = 
    #result = result.difference(b)
    return list(set(range(0,9)).difference(set(a)).difference(set(b)))
    
#print(freeSpaces(a, b), a, b)



def minimax(a, b):
    result = 0
    for c in freeSpaces(a,b):
        newMoveO = b
        newMoveX = a
        #print(c)
        v = int(c)
        #print(v)
        newMoveO.append(v)
        newMoveX.append(v)
        newMoveOresult = wonlost(newMoveO)
        newMoveXresult = wonlost(newMoveX)
        listX =[]
        listO =[]
        listDraw =[]
        #print(listX, listO, listDraw)
        def isThereAWin():
            if newMoveOresult == 2:
                listO.append(int(c))
                True
            elif newMoveOresult == 1 or newMoveXresult == 1:
                listDraw.append(int(c))
                True
            elif newMoveXresult == 2:
                listX.append(int(c))
                True    
            return False
    if isThereAWin() != False:
        if listO != []:
            for x in listO:
                result = x
        elif listX != []:
            for x in listO:
                result = x    
        elif listDraw != []:
            for x in listDraw:
                result = x
    else:
        temp = freeSpaces(a,b)
        if len(temp):
            result = random.choice(temp)
    print()
    return result 
'''
#print(checkDiagonalForward([0,4,8]))
#print(wonlost([0,4,8]))