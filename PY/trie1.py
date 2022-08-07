class Trie:
    
    def __init__(self):
        self.ch = [[0] * 100000 for i in range(26)]
        self.sz = 0
        self.val = [0] * 100000

    def insert(self, word: str) -> None:
        u = 0
        for c in word:
            i = ord(c) - ord('a')
            if self.ch[i][u] == 0:
                self.sz += 1
                self.ch[i][u] = self.sz
            u = self.ch[i][u]
        self.val[u] = 1


    def search(self, word: str) -> bool:
        u = 0
        for c in word:
            i = ord(c) - ord('a')
            if self.ch[i][u] == 0:
                return False
            u = self.ch[i][u]
        return self.val[u] != 0


    def startsWith(self, prefix: str) -> bool:
        u = 0
        for c in prefix:
            i = ord(c) - ord('a')
            if self.ch[i][u] == 0:
                return False
            u = self.ch[i][u]
        return True
        