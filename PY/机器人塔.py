p = [[0] * 510 for i in range(510)]
ans = 0
cnt = 0
x = 1
n, m = map(int, input().split())
while (x + 1) * x // 2 < m + n:
    x += 1

def dfs(cur):
    global ans, cnt
    if cnt > m or cur * (cur + 1) // 2 - cnt > n:
        return
    if cur == x:
        ans += 1
        return
    for i in range(2):
        p[0][cur] = i
        cnt += i
        for j in range(1, cur + 1):
            p[j][cur - j] = p[j - 1][cur - j] ^ p[j - 1][cur - j + 1]
            cnt += p[j][cur - j]
        dfs(cur + 1)
        for j in range(0, cur + 1):
            cnt -= p[j][cur - j]
dfs(0)
print(ans)
