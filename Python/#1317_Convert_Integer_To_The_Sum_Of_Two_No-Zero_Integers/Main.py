class Solution(object):
    def isZero(self, j):
        return "0" not in str(j)


    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            a, b = i, n-i
            if self.isZero(a) and self.isZero(b):
                return [a, b]
