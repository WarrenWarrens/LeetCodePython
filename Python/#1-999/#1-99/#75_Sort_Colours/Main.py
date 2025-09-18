class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[min], nums[i] = nums[i], nums[min]


