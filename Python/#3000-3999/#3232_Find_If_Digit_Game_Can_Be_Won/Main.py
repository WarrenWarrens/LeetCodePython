class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dd = []
        sd = []
        for i in range(len(nums)):
            if nums[i] > 9:
                dd.append(nums[i])
            else:
                sd.append(nums[i])
        if sum(dd) == sum(sd):
            return False
        else:
            return True