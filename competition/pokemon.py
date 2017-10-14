# Kudos to http://www.growingwiththeweb.com/2012/06/a-pathfinding-algorithm.html for a very helpful algorithm and explanation. 
# This made it easy to adapt to the task.

def printMaze(maze):
    for x in range(len(maze)):
        print("")
        for y in range(len(maze[x])):
            print(maze[x][y], end="")
        print("")

def h(n):
    return n[0] - goal[0] + n[1] - goal[1]

def getLowestFScore(stillOpen):
    minIndex = 0
    minScore = stillOpen[0][5]
    for x in range(1, len(stillOpen)):
        if stillOpen[x][5] < minScore:
            minScore = stillOpen[x][5]
            minIndex = x
    return minIndex

def g(item):
    if item == None:
        return 0
    else:
        return g(item[2]) + maze[item[0]][item[1]]

def constructPath(item):
    lowestTotalCost = item[5]
    parent = item[2]
    while parent != None:
        if parent[4] < lowestTotalCost:
            lowestTotalCost = parent[4]
        parent = parent[2]
    if lowestTotalCost > 0:
        print(1)
    else:
        print(abs(lowestTotalCost) + 1)
    return True

def getNext(current):
    nexts = []
    x1 = current[0]+1
    y1 = current[1]
    if x1 <= goal[0] and y1 <= goal[1]:
        gScore1 = g(current) + maze[x1][y1]
        hScore1 = h([x1,y1])
        fScore1 = gScore1 + hScore1
        nexts.append([x1, y1, current, hScore1, gScore1, fScore1])
        
    x2 = current[0]
    y2 = current[1] + 1
    if x2 <= goal[0] and y2 <= goal[1]:
        gScore2 = g(current) + maze[x2][y2]
        hScore2 = h([x2, y2])
        fScore2 = gScore2 + hScore2
        nexts.append([x2, y2, current, hScore2, gScore2, fScore2])
        
    return nexts

def solveMaze(maze, start):
    closed = []
    stillOpen = []
    start[4] = 0
    start[5] = h(start)
    stillOpen.append(start)

    while len(stillOpen) != 0:
        currIndex = getLowestFScore(stillOpen)
        current = stillOpen[currIndex]
        if current[0] == goal[0] and current[1] == goal[1]:
            return constructPath(current)
        stillOpen.pop(currIndex)
        closed.append(current)
        for neighbour in getNext(current):
            inClosed = False
            for x in range(len(closed)):
                if closed[x][0] == neighbour[0] and closed[x][1] == neighbour[1]:
                    inClosed = True
            if inClosed == False:
                neighbour[5] = neighbour[4] + h(neighbour)
                
            inList = False
            for x in range(len(stillOpen)):
                if stillOpen[x][0] == neighbour[0] or stillOpen[x][1] == neighbour[1]:
                    inList = True
            if inList == False:
                stillOpen.append(neighbour)
            else:
                currNeighbour = neighbour
                if g(neighbour) < g(currNeighbour):
                    currNeighbour[4] = neighbour[4]
                    currNeighbour[2] = neighbour[2]
    print("No path found")
     
inter = input()
inputs = inter.split(' ')
r = int(inputs[0])
c = int(inputs[1])

maze = [[0]*c for _ in range(r)]
goal = [r-1, c-1]

for x in range(0, r):
    inter = input()
    inputs = inter.split(' ')
    for y in range(0, c):
        maze[x][y] = int(inputs[y])
        
solveMaze(maze, [0, 0, None, 0, 0, 0])        