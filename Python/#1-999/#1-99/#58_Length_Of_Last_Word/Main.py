class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        index = len(s) - 1

        while index >= 0 and s[index] == " ":
            index = index - 1

        while index >= 0 and s[index] != " ":
            count = count + 1
            index = index - 1

        return count

