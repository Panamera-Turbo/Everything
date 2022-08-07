class edge:
    def __init__(self, u, v, val):
        self.u = u
        self.v = v
        self.val = val
    def __lt__(self, t):
        return self.val < t.val

n, m = map(int, input().split())
fa = [i for i in range(n + 5)]

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

g = []
for i in range(m):
    u, v, val = map(int, input().split())
    g.append(edge(u, v, val))
g.sort()
ans = 0
for i in range(m):
    fu = find(g[i].u)
    fv = find(g[i].v)
    if fu != fv:
        ans = max(ans, g[i].val)
        fa[fu] = fv
ok = True
for i in range(2, n + 1):
    if find(i) != find(1):
        ok = False
if ok:
    print(ans)
else:
    print(-1)
        
