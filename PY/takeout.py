class order:
    def __init__(self, ts, id):
        self.ts = ts
        self.id = id
    def __lt__(self, t):
        return self.ts < t.ts
        

a = []
n, m, t = map(int, input().split())

inque = [False] * (n + 5)
num = [0] * (n + 5)
pre = [0] * (n + 5)
ans = 0
lst = 0
for i in range(m):
    ts, id = map(int, input().split())
    if ts > t:
        continue
    a.append(order(ts, id))

a.sort()
for i in range(m):
    rid = a[i].id
    now = a[i].ts
    if pre[rid] != now:
        num[rid] -= (now - pre[rid] - 1)
    pre[rid] = now
    if num[rid] < 0:
        num[rid] = 0
    if inque[rid] and num[rid] <= 3:
        inque[rid] = False
        ans -= 1
    num[rid] += 2
    if num[rid] > 5 and not inque[rid]:
        ans += 1
        inque[rid] = True
    lst = now
    
for i in range(1, n + 1):
    if inque[i] and num[i] - (t - pre[i]) <= 3:
        ans -= 1
print(ans)

