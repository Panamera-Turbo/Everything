N = int(2e5 + 10)
frac = [0] * N
frac[0] = 1

def qpow(a, b, p):
    a %= p
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        b >>= 1
        a = a * a % p
    return res

def C(n, m, p):
    if m == 0 or n == m:
        return 1
    return frac[n] * qpow(frac[m], p - 2, p) % p * qpow(frac[n - m], p - 2, p) % p

def lucas(n, m, p):
    if m == 0:
        return 1
    return C(n % p, m % p, p) * lucas(n // p, m // p, p) % p

T = int(input())
for cas in range(T):
    n, m, p = map(int, input().split())
    for i in range(1, p):
        frac[i] = frac[i - 1] * i % p
    if p == 1:
        print(0)
    else:
        print(lucas(n + m, m, p) % p)

