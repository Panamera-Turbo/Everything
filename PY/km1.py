N = 105
lx = [0] * N
ly = [0] * N
mch = [0] * N
vs = [False] * N
vt = [False] * N
w = [[] for i in range(N)]
n = 0
lack = int(1e9)

def dfs(u):
    global lack
    vs[u] = True
    for i in range(1, n + 1):
        if vt[i]:
            continue
        t = lx[u] + ly[i] - w[u][i]
        if t == 0:
            vt[i] = True
            if mch[i] == 0 or dfs(mch[i]):
                mch[i] = u
                return True
        else:
            lack = min(lack, t)
    return False

def update():
    for i in range(1, n + 1):
        if vs[i]:
            lx[i] -= lack
        if vt[i]:
            ly[i] += lack

def km():
    for i in range(1, n + 1):
        mch[i] = lx[i] = ly[i] = 0
        for j in range(1, n + 1):
            lx[i] = max(lx[i], w[i][j])
    for i in range(1, n + 1):
        while True:
            for j in range(1, n + 1):
                vs[j] = vt[j] = False
            lack = int(1e9)
            if dfs(i):
                break
            else:
                update()
n = int(input())
for i in range(1, n + 1):
    w[i] = [0] + list(map(int, input().split()))

km()
ans1, ans2 = 0, 0
for i in range(1, n + 1):
    ans1 += lx[i]
    ans1 += ly[i]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        w[i][j] *= -1
km()
for i in range(1, n + 1):
    ans2 += lx[i]
    ans2 += ly[i]
print("{:d}\n{:d}".format(-ans2, ans1))