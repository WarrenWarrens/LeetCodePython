class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = 0
        for num in nums:
            div = set()

            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    div.add(i)
                    div.add(num // i)

                if len(div) > 4:
                    break

            if len(div) == 4:
                totalsum += sum(div)

        return totalsum


