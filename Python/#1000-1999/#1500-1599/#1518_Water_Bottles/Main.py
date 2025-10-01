class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        numEmpty = 0
        numDrank = 0

        while numBottles > 0:
            numDrank += numBottles
            numEmpty += numBottles
            numBottles = 0

            if numEmpty >= numExchange:
                numBottles = numEmpty // numExchange
                numEmpty = numEmpty % numExchange

        return numDrank