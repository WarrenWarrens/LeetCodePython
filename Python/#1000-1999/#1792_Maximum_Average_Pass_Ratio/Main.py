class Solution(object):
    def margain(self, p,t):
        return (p + 1) / (t + 1.0) - (p / float(t))

    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq
        heap1 = []

        for p, t in classes:
            heapq.heappush(heap1, [-self.margain(p,t),p, t])

        for _ in range(extraStudents):
            g,p,t = heapq.heappop(heap1)
            p, t = p + 1, t + 1
            heapq.heappush(heap1, [-self.margain(p,t),p, t])

        total = 0
        while heap1:
            g,p,t = heapq.heappop(heap1)
            total += p / float(t)

        return total / float(len(classes))