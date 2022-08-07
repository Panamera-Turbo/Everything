class Trie:
    def __init__(self, maxnode, sigma_size):
        self.ch = [[0] * sigma_size for i in range(maxnode)]
        self.sz = 0
        self.val = [0] * maxnode
    def idx(self, c):
        return ord(c) - ord('a')
    def insert(self, s, v):
        u = 0
        for c in s:
            i = self.idx(c)
            if self.ch[u][i] == 0:
                self.sz += 1
                self.ch[u][i] = self.sz
            u = self.ch[u][i]
        self.val[u] = v

    def find(self, s):
        u = 0
        for c in s:
            i = self.idx(c)
            if self.ch[u][i] == 0:
                return 0
            u = self.ch[u][i]
        if self.val[u] == 0:
            return 0
        else:
            self.val[u] += 1
            return self.val[u]

T = Trie(300000, 26)
n = int(input())
for i in range(n):
    s = input()
    s = s.strip()
    T.insert(s, 1)
m = int(input())
for i in range(m):
    s = input()
    s = s.strip()
    res = T.find(s)
    if res == 2:
        print("OK")
    elif res == 0:
        print("WRONG")
    else:
        print("REPEAT")
