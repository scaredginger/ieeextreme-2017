for _ in range(int(input())):
    n = int(input())
    ints = [int(i) for i in input().split(' ')]
    ints.sort()
    minNonZeroIndex = 0
    while ints[minNonZeroIndex] == 0:
        minNonZeroIndex += 1
        
    value = ints.pop(minNonZeroIndex)
    ints.append(value)
    
    totalSum = 0
    stringOut = ""
    for x in range(0, len(ints)-1, 1):
        totalSum += ints[x] * ints[x+1]
        stringOut += str(ints[x]) + " "

    stringOut += str(ints[len(ints)-1])       
    print(totalSum)
    print(stringOut)
