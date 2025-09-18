class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod = 1

        def signFunc(x):
            if x == 0:
                return 0
            elif x < 0:
                return -1
            else:
                return 1

        if 0 in nums:
            return signFunc(0)
        else:
            for i in range(len(nums)):
                prod *= nums[i]
            return signFunc(prod)


