class Solution(object):
    def stepSum(self, n):
        if n <= 0:
            return 0
        res, base, step = 0, 1, 1
        while base <= n:
            cnt = min(n, base * 4 - 1) - base + 1
            res += cnt * step
            base *= 4
            step += 1
        return res

    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        an = 0
        for l, r in queries:
            total = self.stepSum(r) - self.stepSum(l - 1)
            an += (total + 1) // 2
        return an




