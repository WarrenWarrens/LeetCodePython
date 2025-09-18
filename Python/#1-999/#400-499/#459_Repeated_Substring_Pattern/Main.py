class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        t = ''
        for i in range(n // 2):
            t += s[i]
            if t * (n // (i + 1)) == s:
                return True
        return False


