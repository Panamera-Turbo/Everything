def exgcd(a, b):
    if b == 0:
        return(1, 0)
    x, y = exgcd(b, a % b)
    return(y, x - a // b * y)

a, b = map(int, input().split())
x, y = exgcd(a, b)
print((x + b) % b)
