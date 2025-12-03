class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        if sum(nums) % k ==0:
            return i
        else:
            while sum(nums) % k != 0:
                l = nums.index(max(nums))
                nums[l] -= 1
                i += 1
            return i