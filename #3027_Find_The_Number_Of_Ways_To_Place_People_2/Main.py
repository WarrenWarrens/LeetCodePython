class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))
        count = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            ylimit = float("-inf")
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if y2 <= y1 and y2 > ylimit:
                    ylimit = y2
                    count += 1

        return count
