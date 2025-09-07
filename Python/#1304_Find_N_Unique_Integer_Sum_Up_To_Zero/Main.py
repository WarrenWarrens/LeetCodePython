class Solution(object):
    def addNumbers(self, rlist, n):
        count = 1
        type = -1
        while len(rlist) != n:
            rlist.append(count * type)
            type *= -1
            if type < 0:
                count += 1
        return rlist

    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rlist = []
        if n % 2 == 0:
            return (self.addNumbers(rlist, n))
        else:
            rlist.append(0)
            return (self.addNumbers(rlist, n))

