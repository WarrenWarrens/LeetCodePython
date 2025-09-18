class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        length = (high - low + 1)

        if low % 2 == 1 and high % 2 == 1:
            count = length // 2 + 1
        else:
            count = length // 2

        return (count)
