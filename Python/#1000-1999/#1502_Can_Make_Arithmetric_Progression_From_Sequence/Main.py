class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        if len(arr) < 2:
            return False
        elif len(arr) <= 1:
            return True
        else:
            for i in range(len(arr) - 2):
                diff1 = arr[i + 1] - arr[i]
                diff2 = arr[i + 2] - arr[i + 1]
                if diff1 != diff2:
                    return False
        return True
