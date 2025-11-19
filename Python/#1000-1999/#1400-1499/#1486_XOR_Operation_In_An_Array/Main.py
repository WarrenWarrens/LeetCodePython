class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        xor_arr = 0
        for i in range(0,n):
            val = start + (2*i)
            nums.append(val)
            xor_arr = xor_arr ^ nums[i]
        return xor_arr