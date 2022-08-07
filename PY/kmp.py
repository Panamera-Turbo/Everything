def kmp(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


s1 = input()
s2 = input()
s2 = s2.replace("\r", "")
s2 = s2.replace("\n", "")
s2 = s2.replace(" ", "")
len2 = len(s2)
s = s2 + "#" + s1
p1 = kmp(s)
n = len(s)
ans = []
for i in range(n):
    if p1[i] == len2:
        print(i - 2 * len2 + 1)
p2 = kmp(s2)
for a in p2:
    print(a, end=" ")
