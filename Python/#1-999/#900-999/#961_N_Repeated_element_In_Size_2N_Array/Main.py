class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        d = []

        for i in range(len(nums)):
            if d.count(nums[i]) == 0:
                if nums.count(nums[i]) == n:
                    return nums[i]
                d.append(nums[i])


