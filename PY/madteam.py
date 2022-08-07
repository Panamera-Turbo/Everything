n = int(input())
A = [list(map(int, input().split())) for i in range(n)]

def check(x):
    s = set()
    for i in range(n):
        res = 0
        for j in range(5):
            if A[i][j] >= x:
                res += 1 << j
        s.add(res)
    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 31:
                    return True
    return False

l, r = 1, int(1e9)
while l < r:
    mid = (l + r + 1) // 2
    if check(mid):
        l = mid
    else:
        r = mid - 1
print(l)
