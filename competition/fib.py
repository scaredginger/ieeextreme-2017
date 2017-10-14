def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n//2)
        c = a*(b*2-a)
        d = a*a+b*b
        if n%2 == 0:
            return (c, d)
        else:
            return (d, c+d)

s = int(input())
result = fib(s)
print((result[1])%(10**9+7))
