class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        middle = 0
        n = len(mat)
        if n % 2 != 0:
            middle = mat[n//2][n//2]
        sum1 = 0
        sum2 = 0
        for i in range(0,len(mat)):
            sum1 += mat[i][i]
        for i in range(len(mat)):
            sum2 += mat[i][len(mat)-1-i]

        return sum2 + sum1 - middle