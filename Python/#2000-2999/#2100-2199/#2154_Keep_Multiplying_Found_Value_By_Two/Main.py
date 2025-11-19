class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        if nums.count(original) == 0:
            return original
        else:
            while nums.count(original) != 0:
                original *= 2
            return original
