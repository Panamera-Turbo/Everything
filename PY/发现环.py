#手写了队列

n = int(input())
g = [[] for i in range(n + 10)]
ind = [0] * (n + 10)
for i in range(n):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    ind[a] += 1
    ind[b] += 1

N = 100005
q = [0] * N
be, ed = 0, 0
for i in range(1, n + 1):
    if ind[i] == 1:
        q[ed] = i
        ed = (ed + 1) % N

while be != ed:
    u = q[be]
    be = (be + 1) % N
    for v in g[u]:
        ind[v] -= 1
        if ind[v] == 1:
            q[ed] = v
            ed = (ed + 1) % N

for i in range(1, n + 1):
    if ind[i] > 1:
        print(i, end=' ')
