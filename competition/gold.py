def printAdjacencyMatrix():
    for x in range(len(adjList)):
        for y in range(len(adjList[x])):
            for z in range(len(adjList[x][y])):
                print(adjList[x][y][z], end="")
            print("")

def getLowestF(openSet):
    minIndex = 0
    minScore = openSet[0][5]
    for x in range(1, len(openSet)):
        if openSet[x][5] < minScore:
            minScore = openSet[x][5]
            minIndex = x
    return minIndex

def h(node):
    return node[0] - goal[0]

def findDistance(index, parId):
    for x in range(1, len(adjList[index])):
        if adjList[index][x][0] == parId:
            return adjList[index][x][1]
            

def g(item):
    if item == None:
        return 0
    else:
        return g(item[2]) + findDistance(item[index] + item[2][0])

def constructPath(item):
    print(item[0])
    parent = item[2]
    while parent != None:
        print(parent[0])
        parent = parent[2]

    return True

def getIndex(nextId):
    for x in range(len(adjList)):
        if adjList[x][0][0] == nextId:
            return adjList[x][0][0] 

def getNext(current):
    nexts = []

    print(adjList[current[1]])
    for x in adjList[current[1]]:
        nextId = x[0]
        nextIndex = getIndex(nextId)
        nextDistance = findDistance(nextIndex, current[0])
        node = [nextId, nextIndex, current, h(nextId), g(current) + nextDistance, h(nextId) + g(current) + nextDistance]
        nexts.append(node)

    return nexts

def findPath(start):
    closedSet = []
    openSet = [start]
    while len(openSet) != 0:
        currIndex = getLowestF(openSet)
        current = openSet[currIndex]
        if current[0] == goal[0]:
            return constructPath(current)
        openSet.pop(currIndex)
        closedSet.append(current)
        for neighbour in getNext(current):
            inOpen = False
            for x in range(len(openSet)):
                if openSet[x][0] == neighbour[0]:
                    inOpen = True
                    break
            if inOpen == False:
                openSet.append(neighbour)
                    
inter = input()
inputs = inter.split(' ')

numCities = int(inputs[0])
connections = int(inputs[1])

smallestId = 100000000
smlIndex = 0
biggestId = 0
bigIndex = 0
adjList = [[0]*2 for _ in range(numCities)]

for x in range(numCities):
    cityId = int(input())
    
    if cityId > biggestId:
        biggestId = cityId
        bigIndex = x
    elif cityId < smallestId:
        smallestId = cityId
        smlIndex = x
        
    adjList[x][0] = [cityId]
    
for y in range(connections):
    inter = input()
    inputs = inter.split(' ')
    a = inputs[0]
    b = inputs[1]
    distance = inputs[2]
    aDone = False
    bDone = False
    for x in range(numCities):
        if aDone == True and bDone == True:
            break;
        if aDone == False and adjList[x][0] == a:
            adjList[x].append([b, distance])
            aDone = True
        elif bDone == False and adjList[x][0] == b:
            adjList[x].append([a, distance])
            bDone = True

printAdjacencyMatrix()
goal = [biggestId, bigIndex]
pathList = findPath([smallestId, smlIndex, None, smallestId-biggestId, 0, smallestId-biggestId])