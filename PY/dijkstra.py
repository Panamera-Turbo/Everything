from queue import Queue, PriorityQueue

class heapnode:
    def __init__(self, d, u):
        self.d = d
        self.u = u
    def __lt__(self, other):
        return self.d < other.d

class edge:
    def __init__(self, to, val):
        self.to = to
        self.val = val

def dijk(n, S, g):
    vis = [False] * (n + 1)
    dis = [0x3f3f3f3f] * (n + 1)
    dis[S] = 0
    q = PriorityQueue()
    q.put(heapnode(0, S))
    while not q.empty():
        a = q.get()
        u = a.u
        if vis[u]:
            continue
        vis[u] = True
        for e in g[u]:
            v = e.to
            if dis[u] + e.val < dis[v]:
                dis[v] = dis[u] + e.val
                q.put(heapnode(dis[v], v))
    INF = (1<<31) - 1
    for i in range(1, n + 1):
        print(dis[i] if dis[i] != 0x3f3f3f3f else INF, end=' ')

n, m, s = map(int, input().split())
g = []
for _ in range(n + 1):
    g.append([])

for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append(edge(v, w))
dijk(n, s, g)