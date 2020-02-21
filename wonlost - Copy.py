# i - horz f/3
# j - vert f%3
def wonlost(dictionary):
    result = 0
    for m in dictionary:
        if len(dictionary[m]) >= 3:
            if checkWin(dictionary) == 3:
                result = 2
            elif 5 == len(dictionary):
                result = 1
        return result

def checkWin(dictionary):
    result = 0
    for m in dictionary:
        if checkDiagonalForward(dictionary) == 3:
            result = 2
        if checkDiagonalBackward(dictionary) == 3:
            result = 2
        if checkHorisontal(dictionary) == 3:
            result = 2
        if checkVertical(dictionary) == 3:
            result = 2		
    return result


def checkDiagonalForward(dictionary):
    result = 0
    for m in dictionary:
        for f in dictionary[m]:
            if f//3 == f%3:
                result+=1
    return result
    
def checkDiagonalBackward(dictionary):
    result = 0
    for m in dictionary:
        for f in dictionary[m]:
            if 3-(f//3)-1 == f%3:
                result+=1
    return result
    
def checkHorisontal(dictionary):
    result = 0
    listI = [0,0,0]
    for m in dictionary:
        for f in dictionary[m]:
            if f//3 == 0:
                listI[0] += 1
            elif f//3 == 1:
                listI[1] += 1
            elif f//3 == 2:
                listI[2] += 1
    return max(listI)
    
def checkVertical(dictionary):
    result = 0
    listJ = [0,0,0]
    for m in dictionary:
        for f in dictionary[m]:
            if f%3 == 0:
                listJ[0] += 1
            elif f%3 == 1:
                listJ[1] += 1
            elif f%3 == 2:
                listJ[2] += 1
    return max(listJ)
    
