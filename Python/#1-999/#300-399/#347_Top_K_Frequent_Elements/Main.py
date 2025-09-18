class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        arr = []
        for _ in range(k):
            max_key = max(freq, key=freq.get)
            arr.append(max_key)
            freq.pop(max_key)
        return arr


