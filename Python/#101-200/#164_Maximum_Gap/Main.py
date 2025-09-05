class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) >= 2:
            nums.sort()
            maxdiff = nums[1] - nums[0]
            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] > maxdiff:
                    maxdiff = nums[i + 1] - nums[i]

            return maxdiff
        else:
            return 0


