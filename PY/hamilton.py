n = int(input())
a = [[] for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

dp = [[int(1e9)] * n for i in range(1<<n)]
dp[1][0] = 0
for i in range(1, 1<<n):
    if i&1:
        for j in range(n):
            if (i>>j) & 1:
                for k in range(n):
                    if k != j and ((i>>k) & 1):
                        dp[i][j] = min(dp[i][j], dp[i - (1<<j)][k] + a[k][j])
print(dp[(1<<n) - 1][n-1])
        
