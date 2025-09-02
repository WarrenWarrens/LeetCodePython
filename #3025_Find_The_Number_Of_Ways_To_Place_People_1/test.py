class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        def sort1(item):
            return item[0], -item[1]

        points.sort(key=sort1)
        r = 0
        for i in range(n - 1):
            top = -1
            for j in range(i + 1, n):
                if top < points[j][1] <= points[i][1]:
                    r += 1
                    top = points[j][1]

        return r