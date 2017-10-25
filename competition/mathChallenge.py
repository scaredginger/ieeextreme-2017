def getBinom(n, k):
    if k == 0:
        return 1
    if k > n/2:
        return  getBinom(n, n - k)
    return n*getBinom(n-1, k-1)//k
    
def digitsOfN(e, base):
    digits = []
    while e:
        digits.append(int(e%base))
        e = e/base
    return digits
    
def fastModExpon(b, e, p, k=5):
    base = 2 << (k-1)

    table = [1]*base
    for x in range(1, base):
        table[x] = table[x-1]*e%p

    r = 1
    for digit in reversed(digitsOfN(e, base)):
        for x in range(k):
            r = r*r%p
        if digit:
            r = r * table[digit] % p
            
    return r

testCases = int(input())

for x in range(testCases):
    inter = input()
    inputs = inter.split(' ')
    a = int(inputs[0])
    b = int(inputs[1])
    c = int(inputs[2])

    result = fastModExpon(a, getBinom(b,c), 10**9+7)
    print(result)
