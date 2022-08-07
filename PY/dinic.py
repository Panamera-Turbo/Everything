from queue import *

tot = 1
g = [0, 0]
N = int(3e3 + 10)
INF = int(1e9)
head = [0] * N
cur = [0] * N
dis = [0] * N
n, m = 0, 0
s, t = 0, 0
class edge:
    def __init__(self, to, nxt, val:int):
        self.to = to
        self.nxt = nxt
        self.val = val

def bfs():
    for i in range(1, n + 1):
        dis[i] = INF
    dis[s] = 0
    cur[s] = head[s]
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        i = head[u]
        while i:
            v = g[i].to
            if g[i].val > 0 and dis[v] == INF:
                cur[v] = head[v]
                dis[v] = dis[u] + 1
                q.put(v)
                if v == t:
                    return True
            i = g[i].nxt
    return False

def dfs(u, a):
    if u == t or a == 0:
        return a
    k, res = 0, 0
    i = cur[u]
    while i:
        cur[u] = i
        v = g[i].to
        if g[i].val > 0 and dis[v] == dis[u] + 1:
            k = dfs(v, min(a, g[i].val))
            if k == 0:
                dis[v] = INF 
            g[i].val -= k
            g[i^1].val += k
            res += k
            a -= k
            if a == 0:
                break
        i = g[i].nxt
    return res

def add(u, v, val):
    global tot
    g.append(edge(v, head[u], val))
    tot += 1
    head[u] = tot



if __name__ == "__main__":
    n, m, s, t= map(int, input().split())  
    for i in range(m):
        u, v, c = map(int, input().split())
        add(u, v, c)
        add(v, u, 0)
    ans = 0
    while bfs():
        #print(1)
        ans += dfs(s, INF)
    print(ans)
