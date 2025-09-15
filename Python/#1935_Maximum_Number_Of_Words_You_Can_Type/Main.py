class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split()
        count = 0

        for word in words:
            if all(ch not in brokenLetters for ch in word):
                count += 1

        return count
