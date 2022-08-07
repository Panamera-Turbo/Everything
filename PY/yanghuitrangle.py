import sys

n = int(input())
a = [[0] * (i + 1) for i in range(2010)]
cnt = 0
ok = False
for i in range(1, 2001):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
        cnt += 1
        if a[i][j] == n:
            print(cnt)
            sys.exit()
for i in range(2, 40001):
    if i * (i - 1) // 2 == n:
        ans = (i + 1) * i // 2
        ans += 3
        print(ans)
        sys.exit()

ans = (n + 1) * n // 2 + 2
print(ans)
        
