def solve(a):
    n, m = len(a), len(a[0])
    a.append([0] * m)
    for i in range(1, n):
        for j in range(m):
            a[i][j] += a[i - 1][j]
    ans = -int(1e9)
    for i in range(n):
        for j in range(i, n):
            dp = [0] * (m + 1)
            res = -int(1e9)
            for k in range(m):
                tmp = a[j][k] - a[i - 1][k]
                dp[k] = max(dp[k - 1] + tmp, tmp)
                res = max(res, dp[k])
            ans = max(ans, res)
    return ans

n, m = map(int, input().split())
a = []
for i in range(n):
    t = list(map(int, input().split()))
    a.append(t)

ans = 0
if n <= m:
    ans = solve(a)
else:
    ta = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            ta[i][j] = a[j][i]
    ans = solve(ta)
print(ans)
            