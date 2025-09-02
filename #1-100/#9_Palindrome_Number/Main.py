class Solution(object):
    def length(self,n):
        if n == 0:
            return 1
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        count = self.length( x)
        y = x
        z = 0

        while count > 0:
            z += (y % 10) * (10 ** (count - 1))
            y //= 10
            count -= 1

        return z == x

