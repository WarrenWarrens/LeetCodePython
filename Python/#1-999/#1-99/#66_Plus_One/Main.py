class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += count
            count = 0
            if digits[i] == 10:
                digits[i] = 0
                count = 1

        if count == 1:
            digits.insert(0, 1)

        return(digits)
