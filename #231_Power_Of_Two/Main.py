class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n <= 0):
            return False
        elif (2147483648 % n == 0):
            return True
        else:
            return False