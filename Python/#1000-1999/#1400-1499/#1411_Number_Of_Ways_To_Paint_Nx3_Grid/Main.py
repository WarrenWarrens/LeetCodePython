class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [[0] * 2 for _ in range(n + 1)]

        dp[1][0] = 6
        dp[1][1] = 6

        for i in range(2, n + 1):
            dp[i][0] = (2 * dp[i - 1][0] + 2 * dp[i - 1][1]) % MOD
            dp[i][1] = (2 * dp[i - 1][0] + 3 * dp[i - 1][1]) % MOD

        return (dp[n][0] + dp[n][1]) % MOD