def getBinom(n, k):
    if k == 0:
        return 1
    if k > n/2:
        return  getBinom(n, n - k)
    return n*getBinom(n-1, k-1)//k

testCases = int(input())

for x in range(testCases):
    inter = input()
    inputs = inter.split(' ')
    a = int(inputs[0])
    b = int(inputs[1])
    c = int(inputs[2])

    print(int((a**getBinom(b,c))%(10**9+7)))
                              
