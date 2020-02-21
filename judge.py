A = [[0,1,2], [3,4,5], [6,7,8]]
K = 0
M = 0
N = []
P = []
n1 = 5
for i in range(len(A)):
    for j in range(len(A[i])):
        for n1 in A[i]:
            if i == j:
                K += K
                print(K)
            if j == 3-i-1:
                M += M
            for n in N:
                N.add(j)
            for p in P:
                P.add(j)
result = 0
if N is 3 or K is 3 or M is 3 or P is 3:
    result = 2
return result