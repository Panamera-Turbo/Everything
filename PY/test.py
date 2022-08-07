class Solution:
    def __init__(self):
        self.mx = 0
        self.ans = 1
    def countMaxOrSubsets(self, nums) -> int:
        n = len(nums)
        self.dfs(nums, [], 0, n)
        print(self.ans)
        return self.ans

    def dfs(self, nums, now, dep, n):
        if dep == n:
            res = 0
            for a in now:
                res |= a
            if res == self.mx:
                self.ans += 1
            elif res > self.mx:
                self.mx = res
                self.ans = 1
            return
        now.append(nums[dep])
        self.dfs(nums, now, dep + 1, n)
        now.pop()
        self.dfs(nums, now, dep + 1, n)