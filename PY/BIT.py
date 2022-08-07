n, m = map(int, input().split())
c = [0] * (n + 10)

def lowbit(x):
    return x & (-x)
def add(x, k):
    while x <= n:
        c[x] += k
        x += lowbit(x)
def query(x):
    ans = 0
    while x >= 1:
        ans += c[x]
        x -= lowbit(x)
    return ans

a = list(map(int, input().split()))
for i in range(len(a)):
    add(i + 1, a[i])
for i in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        add(x, y)
    else:
        print(query(y) - query(x - 1))
