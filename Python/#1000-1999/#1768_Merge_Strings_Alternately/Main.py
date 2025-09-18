class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newstr = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                newstr += word1[i]
                newstr += word2[i]
        elif len(word1) > len(word2):
            for i in range(len(word1)):
                newstr += word1[i]
                if i < len(word2):
                    newstr += word2[i]
        else:
            for i in range(len(word2)):
                if i < len(word1):
                    newstr += word1[i]
                newstr += word2[i]

        return newstr
