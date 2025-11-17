class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = x
            rev = 0
            while y !=0:
                digit = y % 10
                rev = rev * 10 + digit
                y //= 10
            if rev != x:
                return False
            else:
                return True
