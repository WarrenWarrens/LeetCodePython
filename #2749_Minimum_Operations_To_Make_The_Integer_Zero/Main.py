class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1, 61):
            tar = num1 - num2 * k
            if tar < 0:
                continue
            bits = bin(tar).count("1")
            if bits <= k <= tar:
                return k
        return -1
