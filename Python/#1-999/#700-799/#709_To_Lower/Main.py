class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = ""

        for i in s:
            if 65 <= ord(i) <= 90:
                n += chr(ord(i) + 32)
            else:
                n += i

        return n

