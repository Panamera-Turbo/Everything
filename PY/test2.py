from queue import *

n, k = map(int, input().split())
m = [[] for i in range(305)]
vis = [[False] * 305 for i in range(305)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
q = Queue()
wt = 2

for i in range(1, n + 1):
    m[i] = [" "] + list(input())

q.put((3, 3, 0))
vis[3][3] = True

def check(x, y, wt):
    if x + wt > n or y + wt > n or x - wt < 1 or y - wt < 1 or vis[x][y]:
        return False
    for i in range(x - wt, x + wt + 1):
        for j in range(y - wt, y + wt + 1):
            #print(i, j)
            if m[i][j] == "*":
                return False
    return True

ans = 0
while not q.empty():
    x, y, tm = q.get()
    if x == n - 2 and y == n - 2:
        ans = tm
        break
    if tm < k:
        wt = 2
    elif tm < 2 * k:
        wt = 1
    else:
        wt = 0
    if wt != 0:
        q.put((x, y, tm + 1))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if check(nx, ny, wt):
            q.put((nx, ny, tm + 1))
            vis[nx][ny] = True
print(ans)
        









    

