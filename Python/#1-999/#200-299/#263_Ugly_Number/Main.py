class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            fact = [2, 3, 5]
            for i in fact:
                while n % i == 0:
                    n = n / i
            return n == 1
        else:
            return False







