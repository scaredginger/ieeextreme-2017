#def printMatrix(m):
#    for x in range(4):
#        print("")
#        for y in range(4):
#            print(str(m[x][y]) + " ", end="")
#    print("")

def checkForCycle(adjacencyMatrix, maxNum):
    for x in range(0, maxNum+1):
        for y in range(1, maxNum+1):
            if adjacencyMatrix[x][y] == 1:
                #go to the y'th row and try and find a similar element
                for p in range(0, maxNum+1):
                    if adjacencyMatrix[y][p] == 1:
                        #check if column matches
                        if adjacencyMatrix[x][p] == 1:
                            return True
    return False
        

if __name__ == "__main__":

    tests = int(input())
    for x in range(tests):

        inter = input()
        inputs = inter.split(' ')
        vertices = int(inputs[0])
        edges = int(inputs[1])

        maxVertex = 0
        inter = input()
        inputs = inter.split(' ')
        inputs = list(map(int, inputs))
        maxNum = max(inputs)

        adjacencyMatrix = [[0]*(maxNum+1) for _ in range(maxNum+1)]
        
        for z in range(edges):

            a = int(inputs[2*z])
            b = int(inputs[2*z+1])
                
            if a==b:
                print(1)
                break
            else:
                adjacencyMatrix[a][b] = 1
                adjacencyMatrix[b][a] = 1

        if checkForCycle(adjacencyMatrix, maxNum) == True:
            print(1)
        else:
            print(0)
    
    
