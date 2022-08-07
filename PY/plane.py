n = int(input())
line = []
for i in range(n):
    k, b = map(int, input().split())
    line.append((k, b))
line = list(set(line))
n = len(line)
ans = 2
def judge(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) < 1e-18

for i in range(1, n):
    k1, b1 = line[i]
    sec = []
    for j in range(i):
        k2, b2 = line[j]
        if k1 == k2:
            continue
        posx = (b2 - b1) / (k1 - k2)
        posy = posx * k1 + b1
        sec.append((posx, posy))
    m = len(sec)
    tmpans = m + 1
    if m < 2:
        ans += tmpans
    else:
        sec.sort()
        for i in range(1, m ):
            if judge(sec[i], sec[i - 1]):
                tmpans -= 1
        ans += tmpans
print(ans)
