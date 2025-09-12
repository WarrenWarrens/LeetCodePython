class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = "aeiouAEIOU"
        if any(ch in vowels for ch in s):
            return (True)
        else:
            return (False)


