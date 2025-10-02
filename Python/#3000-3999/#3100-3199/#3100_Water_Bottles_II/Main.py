class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        numEmpty = 0
        numDrank = 0

        while numBottles > 0 or numEmpty >= numExchange:
            if numBottles > 0:
                numDrank += numBottles
                numEmpty += numBottles
                numBottles = 0

            if numEmpty >= numExchange:
                numEmpty -= numExchange
                numBottles += 1
                numExchange += 1

        return numDrank
