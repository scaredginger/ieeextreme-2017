import sys
# functions used to comunicate with the interactor (the other program)
# use this to the edge newly added edge.
# after using it you must provide your answer
# TL;DR get_edge() get_edge() is invalid
def get_edge():
    inter = input()
    inputs = inter.split(' ')
    a = int(inputs[0])-1
    b = int(inputs[1])-1
    return a, b
    
def get_number():
    n = int(input())
    return n

# use this to set your answer
def set_answer(s):
    print(s)
    sys.stdout.flush()
    
def checkForCycle(visited, left):
    count = 0
    while len(left) != 0:
        current = left[0]
        visited.append(current)
        left.pop(0)
        
        for x in range(1, len(adjList[current])-1):
            if adjList[current][x] not in visited:
                left.append(adjList[current][x])
            else:
                #cycle is found, check if its odd length
                if count%2 == 0:
                    return 0
        count += 1
        
    return 1        
    
def addEdge(edge):
    adjList[edge[0]].append(edge[1])
    adjList[edge[1]].append(edge[0])
    
    visited = []
    left = []
    visited.append(edge[1])
    visited.append(edge[0])
    
    for x in range(1, len(adjList[edge[0]])-1):
        left.append(adjList[edge[0]][x])
        
    result = checkForCycle(visited, left)
    return result
    
playing = True
n = get_number()

adjList = []
for x in range(n):
    adjList.append([x])

while playing:
    edge = get_edge()
    answer = addEdge(edge)
    set_answer(answer)
    if answer == 0:
        playing = False
