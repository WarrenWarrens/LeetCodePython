class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        if len(accounts) <= 1:
            if len(accounts) == 0:
                return 0
            else:
                return sum(accounts[0])
        else:
            max = sum(accounts[0])
            for i in accounts:
                if sum(i) > max:
                    max = sum(i)
            return max
