class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        i = 0
        num1 = []
        num2 = []
        while i <= n:
            if i % m == 0:
                num2.append(i)
            else:
                num1.append(i)
            i += 1
        return sum(num1) - sum(num2)

