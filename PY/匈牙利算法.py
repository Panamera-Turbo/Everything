n, m, t = map(int, input().split())
g = [[] for i in range(n + m + 10)]
vist = [0] * (n + m + 10)
mch = [0] * (n + m + 10)
for i in range(t):
    u, v = map(int, input().split())
    g[u].append(v)
ans = 0
def dfs(u, tag):
    if vist[u] == tag:
        return False
    vist[u] = tag
    for v in g[u]:
        if mch[v] == 0 or dfs(mch[v], tag):
            mch[v] = u
            return True
    return False

for i in range(1, n + 1):
    if dfs(i, i):
        ans += 1
print(ans)
