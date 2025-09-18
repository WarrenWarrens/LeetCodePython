class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isIncrease = True
        isDecrease = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                isDecrease = False
            elif nums[i] < nums[i - 1]:
                isIncrease = False

        return isIncrease or isDecrease