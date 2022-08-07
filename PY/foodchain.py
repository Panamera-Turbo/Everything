n ,k = map(int, input().split())
fa = [i for i in range(3 * n + 10)]

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

ans = 0
for i in range(k):
    op, x, y = map(int, input().split())
    if x > n or y > n:
        ans += 1
        continue
    if op == 1:
        if find(x + n) == find(y) or find(x) == find(y + n):
            ans += 1
        else:
            fa[find(x)] = find(y)
            fa[find(x + n)] = find(y + n)
            fa[find(x + 2 * n)] = find(y + 2 * n)
    else:
        if find(x) == find(y) or find(x + n) == find(y):
            ans += 1
        else:
            fa[find(x)] = find(y + n)
            fa[find(x + n)] = find(y + 2 * n)
            fa[find(x + 2 * n)] = find(y)
print(ans)
        
