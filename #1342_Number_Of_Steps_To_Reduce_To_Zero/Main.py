class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0 or num < 0:
            return 0
        else:
            count = 0
            while num > 0:
                if num % 2 == 0:
                    num /= 2
                else:
                    num -= 1
                count += 1

            return count
