class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minval = min(nums)
        maxval = max(nums)

        count = [0] * (maxval - minval + 1)

        for i in nums:
            count[i - minval] += 1

        rem = k
        for i in range(len(count) - 1, -1, -1):
            rem -= count[i]

            if rem <= 0:
                return i + minval

