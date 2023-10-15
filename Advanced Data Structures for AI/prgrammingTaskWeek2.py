from random import random

def dotProduct(matrix1, matrix2):
    isEven = False
    rowSize = len(matrix1[0])
    columnSize = len(matrix1)

    for i in range(0, len(matrix1)):
        if len(matrix1[i]) == rowSize:
            isEven = True
        else:
            isEven = False
            break
                        
    if (rowSize == len(matrix2) and isEven == True):                
        finalArray = [0]*columnSize
        for i in range(0, columnSize):
            temp=0
            for j in range(0, rowSize):
                temp += (matrix1[i][j] and matrix2[j])
            if (temp%2 == 0):
                finalArray[i] = 0
            else:
                finalArray[i] = 1   
        return(finalArray)
    
    else:
        return(print("Invalid inputs"))

def returnRandomHashFunction(m,n):
    hashFunction = [0] * m
    for i in range(m):
        hashFunction[i] = [0] * n
        for j in range(n):
            temp = 0
            randVal = random()
            assert randVal > 0
            if (randVal >= 0.5):
                hashFunction[i][j] = 1
            else:
                hashFunction[i][j] = 0
    return hashFunction

# for the test case example given on moodle:

key = 14
keyBinary = [1,1,1,0]
n = 4
m = 3  
H = returnRandomHashFunction(m,n)

hashValue = dotProduct(H, keyBinary)
print("hash function is as follows: ", H)
print("hash value is as follows: ", hashValue)



            