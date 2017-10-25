def checkForLoops(adjacencyList, common, index):

    if len(adjacencyList[index]) < 1:
        print(x+1)
    else:
        for x in range(len(adjacencyList[index])):
            if adjacencyList[index][x] in common and adjacencyList[index][x] :
                break
            common.append(adjacencyList[index][x])

inter = input()
inputs = inter.split(' ')
numCities = int(inputs[0])
numRoads = int(inputs[1])
adjacencyList = [[] for _ in range(numRoads+1)]

for x in range(numRoads):

    inter = input()
    inputs = inter.split(' ')

    a = int(inputs[0])-1
    b = int(inputs[1])-1

    #REMEMEBER TO CHANGE INDEXES WHEN PRINTING TO BE ONE INDEXED

    adjacencyList[a].append(b)
    adjacencyList[b].append(a)

result = checkForLoops(adjacencyList, [], 0)
result.sort()
for x in result:
    print(x)

    
