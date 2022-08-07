N = 100010
s = [0] * (N<<2)
add = [0] * (N<<2)

def pushup(rt):
    s[rt] = s[rt<<1] + s[rt<<1|1]
def pushdown(rt, L, R):
    if add[rt] != 0:
        M = (L + R) // 2
        s[rt<<1] += (M - L + 1) * add[rt]
        s[rt<<1|1] += (R - M) * add[rt]
        add[rt<<1] += add[rt]
        add[rt<<1|1] += add[rt]
        add[rt] = 0
def update(rt, L, R, ql, qr, val):
    if ql <= L and qr >= R:
        s[rt] += (R - L + 1) * val
        add[rt] += val
        return
    M = (L + R) // 2
    pushdown(rt, L, R)
    if ql <= M:
        update(rt<<1, L, M, ql, qr, val)
    if M + 1 <= qr:
        update(rt<<1|1, M + 1, R, ql, qr, val)
    pushup(rt)
def query(rt, L, R, ql, qr):
    if ql <= L and qr >= R:
        return s[rt]
    M = (L + R) // 2
    pushdown(rt, L, R)
    res = 0
    if ql <= M:
        res += query(rt<<1, L, M, ql, qr)
    if M + 1 <= qr:
        res += query(rt<<1|1, M + 1, R, ql, qr)
    return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    update(1, 1, n, i + 1, i + 1, a[i])
for i in range(m):
    ops = list(map(int, input().split()))
    if len(ops) == 4:
        update(1, 1, n, ops[1], ops[2], ops[3])
    else:
        print(query(1, 1, n, ops[1], ops[2]))
    
