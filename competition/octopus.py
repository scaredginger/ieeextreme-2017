def getScore(board, n, m):
    watches = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                watches += 1
    return watches

def printBoard(board, n, m):
    for i in range(n):
        print("")
        for j in range(m):
            print(str(board[i][j]) + " ", end="")
        print("")

inter = input()
inputs = inter.split(' ')
n = int(inputs[0])
m = int(inputs[1])

board =  [[0]*m for _ in range(n)]
for i in range(n):
    inter = input()
    inputs = inter.split(' ')
    for j in range(m):
        board[i][j] = int(inputs[j])%3

rowSumIndex = 0
bestRowSum = 0
mult = [0]*n

for _ in range(n):
    for x in range(n):
        rowSum0 = 0
        rowSum1 = 0
        rowSum2 = 0
        for y in range(m):
            if board[x][y] == 1:
                rowSum1 += 1
            elif board[x][y] == 2:
                rowSum2 += 1
            else:
                rowSum0 += 1
            if rowSum1 > rowSum2 and rowSum1 > rowSum0:
                mult[x] = 2
                bestSum = rowSum1
            elif rowSum2 >= rowSum1 and rowSum2 > rowSum0:
                mult[x] = 1
                bestSum = rowSum2
        if bestSum > bestRowSum:
            bestRowSum = bestSum
            rowSumIndex = x

    for y in range(m):
        print("changing" + str(rowSumIndex))
        temp = board[rowSumIndex][y]
        temp += mult[rowSumIndex]
        temp = temp%3
        board[rowSumIndex][y] = temp

printBoard(board, n, m)
print(getScore(board, n, m))
        
        
        

