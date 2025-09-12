class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        x1 = coordinates[1][0]
        y1 = coordinates[1][1]
        dx = x1 - x0
        dy = y1 - y0

        for i in range(2, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
                return False
        return True