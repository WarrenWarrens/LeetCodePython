class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        modnum = 0
        result = []

        for bit in nums:
            modnum = (modnum * 2 + bit) % 5
            result.append(modnum == 0)

        return result