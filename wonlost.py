# i - horz f/3
# j - vert f%3
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
    
#print(checkDiagonalForward([0,4,8]))
#print(wonlost([0,4,8]))