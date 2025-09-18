class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_arr = heights[:]

        count = 0
        swap = True
        while swap:
            swap = False
            for i in range(len(sorted_arr) - 1):
                if sorted_arr[i] > sorted_arr[i + 1]:
                    sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                    swap = True

        for i in range(len(sorted_arr)):
            if sorted_arr[i] != heights[i]:
                count += 1

        return(count)
