class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        wordcountlist = []
        for i in range(len(sentences)):
            wordcount = 1
            for j in range(len(sentences[i])):
                if sentences[i][j] == ' ':
                    wordcount += 1
            wordcountlist.append(wordcount)

        return max(wordcountlist)