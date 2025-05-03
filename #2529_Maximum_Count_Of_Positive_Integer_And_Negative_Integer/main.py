class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        neg = 0
        for x in nums:
            if x < 0:
                neg = neg + 1
            if x > 0:
                pos = pos + 1

        if neg < pos:
            return pos
        elif neg > pos:
            return neg
        else:
            return neg
