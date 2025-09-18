class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squarelist = []
        for i in range(len(nums)):
            squarelist.append(nums[i] ** 2)
        squarelist.sort()
        return squarelist
