from queue import *

N = 10050
g = [[] for i in range(N)] # to val
inque = [False] * N
dis = [(1<<31) - 1] * N
cnt = [0] * N
n = 0

def spfa(s):
    dis[s] = 0
    q = Queue()
    q.put(s)
    inque[s] = True
    while not q.empty():
        u = q.get()
        inque[u] = False
        for e in g[u]:
            v = e[0]
            if dis[u] + e[1] < dis[v]:
                dis[v] = dis[u] + e[1]
                if not inque[v]:
                    q.put(v)
                    cnt[v] += 1
                    if cnt[v] > n:
                        return False
    for i in range(1, n + 1):
        print(dis[i], end=' ')
    return True

n, m, s = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
spfa(s)

