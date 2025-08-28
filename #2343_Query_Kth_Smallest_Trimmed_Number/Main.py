class Solution(object):
    def counting_sort(self, ind, nums, digipos):
        buckets = [[] for _ in range(10)]

        for idx in ind:
            digit = int(nums[idx][digipos])
            buckets[digit].append(idx)

        newind = []
        for i in range(10):
            newind.extend(buckets[i])

        return newind

    def pre(self, nums):
        n = len(nums)
        l = len(nums[0])
        precomp = dict()

        ind = list(range(n))

        for digipos in range(l - 1, -1, -1):
            ind = self.counting_sort(ind, nums, digipos)

            trim = l - digipos
            precomp[trim] = ind[:]

        return precomp

    def answer(self, nums, queries):
        precomp = self.pre(nums)
        results = []
        for (K, trim) in queries:
            order = precomp[trim]
            results.append(order[K - 1])
        return results

    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        return self.answer(nums, queries)


