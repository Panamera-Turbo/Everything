import sys  
sys.setrecursionlimit(1000000) #例如这里设置为一百万

N = int(1e5 + 10)
lg = [0] * N
g = [[] for i in range(N)]
fa = [[0] * 35 for i in range(N)]
dep = [0] * N

def dfs(u, f):
    dep[u] = dep[f] + 1
    fa[u][0] = f
    for i in range(1, lg[dep[u]] + 1):
        fa[u][i] = fa[fa[u][i - 1]][i - 1]
    for v in g[u]:
        if v != f:
            dfs(v, u)


def lca(x, y):  # 假定x为祖先
    while (dep[x] < dep[y]):
        y = fa[y][lg[dep[y] - dep[x]]]
    return x == y

    
n, q = map(int, input().split())
lg[0] = -1
for i in range(1, n + 1):
    lg[i] = lg[i >> 1] + 1

for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)

dfs(1, 0)
for i in range(q):
    x, y = map(int, input().split())
    if dep[x] > dep[y]:
        print("NO")
    else:
        if lca(x, y):
            print("YES")
        else:
            print("NO")





