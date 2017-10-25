def findLast(string, find, lastIndex):

    for x in range(lastIndex-1, -1, -1):
        if string[x] == find:
            return x
    return -1

s = input()
q = int(input())
for _ in range(q):
    p = input()
    
    sliceIndex = 1
    lastIndex = findLast(s, p[-1:], len(s))
    
    while lastIndex > -1:
        lastIndex = findLast(s, p[-sliceIndex-1:-sliceIndex], lastIndex)
        sliceIndex += 1
        
    print(sliceIndex - 1)
        
