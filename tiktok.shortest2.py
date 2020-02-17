dictionary = {'x': [], 'o': []}
a = dictionary['x']
b = dictionary['o']
k = 0
comb = [[0, 1, 2],[0, 4, 8],[0, 3, 6],[1, 4, 7],[2, 4, 6],[2, 5, 8],[3, 4, 5],[6, 7, 8]]
def wonlost():
    for m in dictionary:
        s = dictionary[m]
        for f in comb:
                if f[0] in s and f[1] in s and f[2] in s:
                    print("won!")
                    break

from appearanceAB2 import appearance
appearance(a, b)
#from won import wonlost1
conin = ''
def end():
    print("End of the game, thanks for playing!")
def mywhile():
    k = True
    while k == True:
        for m in dictionary:
            s = dictionary[m]
            def intconin():
                conin = input()
                if conin == '':
                    end()
                    global k
                    k = False
                    print("Please press Enter to exit.")
                elif conin.isdigit():
                    n1 = int(conin) - 1
                    if n1 in a or n1 in b or n1 > 9 or n1 < 0:
                        print("Use another number:")
                        intconin()
                    else:
                        s.append(n1)
                        appearance(a, b)
                        wonlost()
                else:
                    print("Please enter a digit:")
                    intconin()
            intconin()
 #           print(a, b, "draw")
mywhile()


