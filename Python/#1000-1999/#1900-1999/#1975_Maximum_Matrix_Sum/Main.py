class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        sumtotal = 0
        negcount = 0
        smallval = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                sumtotal += abs(val)

                if val < 0:
                    negcount += 1

                if abs(val) < smallval:
                    smallval = abs(val)

        if negcount % 2 == 0:
            return sumtotal

        else:
            return sumtotal - (2 * smallval)