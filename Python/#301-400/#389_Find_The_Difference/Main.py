class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return t
        else:
            for i in range(len(t)):
                if s.count(t[i]) != t.count(t[i]):
                    return t[i]
