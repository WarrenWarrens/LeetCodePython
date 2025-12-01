class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        left = 1
        right = sum(batteries) / n

        while left < right:
            tar = (left + right + 1) // 2
            extra = sum(min(battery, tar) for battery in batteries)

            if extra >= n * tar:
                left = tar

            else:
                right = tar - 1

        return left
