class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1 or nums.count(0) == 0:
            exit
        else:
            count = nums.count(0)

            for i in range(count):
                nums.append(0)

            i = 0
            while i < len(nums):
                if nums[i] == 0:
                    nums.pop(i)
                else:
                    i += 1
            nums.extend([0] * count)