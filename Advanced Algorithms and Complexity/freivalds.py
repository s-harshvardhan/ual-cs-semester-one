import random

A = [[2, 3], [3, 4]]
B = [[1, 0], [1, 2]]
C = [[5, 6], [7, 8]]

def matrixMultiplication(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            product = 0
            for v in range(len(A[i])):
                product += A[i][v] * B[v][j]
            row.append(product)
        result.append(row)
    return result

def freivalds(A, B, C):
    n = len(A)
    r = []
    for i in range(0, n):
        r.append([random.randint(0, 1)])

    # brute force validation method:    
        # if matrixMultiplication(A, B) == C:    
        #     return True
        # else:
        #     return False
    temp1 = matrixMultiplication(A, matrixMultiplication(B, r))
    temp2 = matrixMultiplication(C, r)
    P = []
    for i in range(0, n):
        P.append(temp1[i][0] - temp2[i][0])
    # print(sum(P))
    # print(sum(P))
    if sum(P) == 0:
        return True
    else:
        return False
    
print(freivalds(A, B, C))
