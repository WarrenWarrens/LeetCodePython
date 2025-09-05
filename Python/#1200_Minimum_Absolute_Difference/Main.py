class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        mindiff = float('inf')
        for i in range(len(arr) - 1):
            mindiff = min(mindiff, arr[i + 1] - arr[i])

        newarr = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == mindiff:
                newarr.append([arr[i], arr[i + 1]])

        return (newarr)

