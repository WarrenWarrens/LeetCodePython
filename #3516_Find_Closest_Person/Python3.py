class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz = abs(z - x)
        yz = abs(z - y)

        if x == y == z or xz == yz:
            return 0
        elif xz < yz:
            return 1
        else:
            return 2
