n = int(input())
a = list(map(int, input().split()))
v = []

def lower_bound(v, x):
    l, r = 0, len(v) - 1
    while l < r:
        mid = (l + r) // 2
        if v[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l
for x in a:
    if len(v) == 0 or x > v[-1]:
        v.append(x)
    else:
        pos = lower_bound(v, x)
        v[pos] = x
print(len(v))
        
