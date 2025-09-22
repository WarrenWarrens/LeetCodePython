from collections import Counter


class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        maxfreq = max(freq.values())
        result = sum(v for v in freq.values() if v == maxfreq)
        return result

