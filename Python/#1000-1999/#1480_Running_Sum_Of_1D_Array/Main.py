class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        list = []
        for i in nums:
            sum += i
            list.append(sum)
        return list