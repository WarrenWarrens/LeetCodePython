class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        i = 0
        j = len(directions) - 1
        col = 0

        while i <= j and directions[i] == 'L':
            i += 1

        while j >= i and directions[j] == 'R':
            j -= 1

        for k in range(i, j + 1):
            if directions[k] != 'S':
                col += 1

        return col