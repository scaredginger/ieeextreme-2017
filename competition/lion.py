def printMatrix():
    for x in range(len(matrix)):
        print("")
        for y in range(len(matrix[x])):
            print(matrix[x][y], end="")
        print("")

def manDist(row, col, x, y, man):
    return abs(row-x) + abs(col-y) <= man

def fillDistance(row, col, dist):
    a = col-dist
    b = col+dist
    f = row+dist
    e = row-dist
    for x in range(a, b+2):
        for y in range(e, f+2):
            if x >= 0 and x < m and y >= 0 and y < n:
                if manDist(row, col, x, y, dist):
                    matrix[x][y] += 1

inter = input()
inputs = inter.split(' ')

n = int(inputs[0])
m = int(inputs[1])
k = int(inputs[2])

matrix = [[0]*n for _ in range(m)]
lionPos = []

for x in range(k):
    inter = input()
    inputs = inter.split(' ')
    row = int(inputs[0])-1
    col = int(inputs[1])-1
    lionPos.append([row, col])
    dist = int(inputs[2])
    fillDistance(row, col, dist)
    #printMatrix()

maxNumber = 0
bestLionIndex = 0
for x in range(len(lionPos)):
    if matrix[lionPos[x][1]][lionPos[x][0]] > maxNumber:
        bestLionIndex = x+1
        maxNumber = matrix[lionPos[x][1]][lionPos[x][0]]
        
print(bestLionIndex, maxNumber)
    
    
    
