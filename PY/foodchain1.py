n ,k = map(int, input().split())
fa = [i for i in range(n + 10)]
val = [0 for i in range(n + 10)]

def find(x):
    if fa[x] != x:
        t = fa[x]
        fa[x] = find(fa[x])
        val[x] = (val[x] + val[t]) % 3
    return fa[x]

ans = 0
for i in range(k):
    op, x, y = map(int, input().split())
    if x > n or y > n:
        ans += 1
        continue
    else:
        fx, fy = find(x), find(y)
        if fx == fy:
            if op - 1 != (val[x] - val[y] + 3) % 3:
                ans += 1
        else:
            fa[fx] = fy
            val[fx] = (-val[x] + op - 1 + val[y] + 3) % 3
print(ans)
        
