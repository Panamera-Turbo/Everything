class st:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
        self.sum = u + v + w
    def __lt__(self, tmp):
        if self.sum == tmp.sum:
            return self.u + self.v < tmp.u + tmp.v
        return self.sum < tmp.sum

a = []
n = int(input())
for i in range(n):
    u, v, w = map(int, input().split())
    t = st(u, v, w)
    a.append(t)
a.sort()
ans = 0
tm = 0
for i in range(n):
    tm += (a[i].u + a[i].v)
    ans += tm
    tm += a[i].w
print(ans)
