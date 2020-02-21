g = 1
h = 1
def minimax(a, b):
    move = -1
    score = -2    
    for c in freeSpaces:
        newMoveO = b
        newMoveX = a
        newMoveO.append(c)
        newMoveX.append(c)
        newMoveOresult = wonlost(newMove)
        newMoveXresult = wonlost(newMove)
        def scoreForTheMove():
            if newMoveOresult == 2:
                result += 1
            elif newMoveOresult == 1 or newMoveXresult == 1:
                result = 0
            elif newMoveXresult == 2:
                result -= 1
            return result
        if scoreForTheMove() > score:
                score = scoreForTheMove
                conin = int(c)
    