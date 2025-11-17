class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = [i for i in range(len(nums)) if nums[i] == 1]

        for j in range(1, len(pos)):
            if pos[j] - pos[j - 1] - 1 < k:
                return False

        return True




