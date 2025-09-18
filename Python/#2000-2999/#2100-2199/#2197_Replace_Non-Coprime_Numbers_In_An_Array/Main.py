class Solution(object):
    def GCD(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def LCM(self, a, b):
        return (a * b) // self.GCD(a, b)

    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stck = []
        for i in nums:
            stck.append(i)

            while len(stck) > 1:
                a = stck[-1]
                b = stck[-2]
                if self.GCD(a, b) > 1:
                    lcm_val = self.LCM(a, b)
                    stck.pop()
                    stck.pop()
                    stck.append(lcm_val)
                else:
                    break

        return (stck)

