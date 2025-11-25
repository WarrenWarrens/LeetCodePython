class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        diglist = [int(x) for x in str(n)]
        sum = 1
        prod = 0
        for i in range(len(diglist)):
            sum *= diglist[i]
            prod += diglist[i]

        return sum - prod
