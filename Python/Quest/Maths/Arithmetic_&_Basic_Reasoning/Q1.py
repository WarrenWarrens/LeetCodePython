class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort(reverse=True)
        for i in range(1, len(arr) - 1):
            if abs(arr[i] - arr[i - 1]) != abs(arr[i + 1] - arr[i]):
                return False
        return True

