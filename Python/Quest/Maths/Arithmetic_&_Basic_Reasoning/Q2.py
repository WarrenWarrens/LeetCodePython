class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) // 2

        for x in range(1, n + 1):
            left = x * (x + 1) // 2
            right = total - (x * (x - 1) // 2)
            if left == right:
                return x

        return -1

