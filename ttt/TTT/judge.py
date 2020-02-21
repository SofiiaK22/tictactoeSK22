winCombi = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def checkWin(turnsList):
    for c in winCombi:
        if c[0] in turnsList and c[1] in turnsList and c[2] in turnsList:
            return c
    return []

# i - horz f/3
# j - vert f%3

def checkDiagonalForward(turnsList):
	result = 0
	for f in turnsList:
		if f//3 == f%3:
			result+=1
	return result\]-
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
		if f//3 == 0:
			listI[0] += 1
		elif f//3 == 1:
			listI[1] += 1
		elif f//3 == 2:
			listI[2] += 1

	return max(listI)
	
def checkVertical(turnsList):
	result = 0
	listJ = [0,0,0]
	for f in turnsList:
		if f%3 == 0:
			listJ[0] += 1
		elif f%3 == 1:
			listJ[1] += 1
		elif f%3 == 2:
			listJ[2] += 1
	return max(listJ)
	
def checkWin2(turnsList):
	result = 0
	if checkDiagonalForward(turnsList) == 3:
		result = 1
	if checkDiagonalBackward(turnsList) == 3:
		result = 1
	if checkHorisontal(turnsList) == 3:
		result = 1
	if checkVertical(turnsList) == 3:
		result = 1		
	return result

def judge(turnsList):
    result = 0
    if len(turnsList) >= 3:
        if checkWin2(turnsList) == 1:
            result = 2
        else:
            if 5 == len(turnsList):
                result = 1
    return result
