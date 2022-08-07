MOD = int(1e9 + 7)

s = " " + input()
n = len(s) - 1

def solve(s):
    global n, MOD
    add = [0] * 5005
    sm = [[0] * 5005 for i in range(5005)]
    f = [[0] * 5005 for i in range(5005)]
    num, lnum, rnum = 0, 0, 0
    for i in range(1, n + 1):
        if s[i] == "(":
            lnum += 1
        else:
            num += 1
            rnum += 1
            if lnum:
                lnum -= 1
                rnum -= 1
            add[num] = rnum
    for i in range(add[1], n + 1):
        f[1][i] = 1
        if i == 0:
            sm[1][i] = 1
        else:
            sm[1][i] = (sm[1][i - 1] +  f[1][i]) % MOD

    for i in range(2, num + 1):
        for j in range(0, add[i] + 1):
            f[i][add[i]] = (f[i][add[i]] + f[i - 1][j]) % MOD
        sm[i][add[i]] = f[i][add[i]]
        for j in range(add[i] + 1, n + 1):
            f[i][j] = sm[i - 1][j]
            sm[i][j] = (sm[i][j - 1] + f[i][j]) % MOD
    return f[num][rnum]

ans = solve(s)

ts = ""
for c in s:
    if c == "(":
        ts += ")"
    elif c == ")":
        ts += "("
        
ans = ans * solve(" " + ts[::-1])
print(ans)
        
