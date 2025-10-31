class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        done = []
        for i in range(len(nums)):
            if done.count(i) == 0:
                if nums.count(i) >= 2:
                    arr.append(i)
                if len(arr) >= 2:
                    return arr
            else:
                done.append(i)

        return arr


