class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        xz = abs(z - x)
        yz = abs(z - y)

        if x == y == z or xz == yz:
            return 0
        elif xz < yz:
            return 1
        else:
            return 2
