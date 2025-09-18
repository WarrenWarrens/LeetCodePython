class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        arrMatch = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i].lower() in words[j].lower() and words[i] not in arrMatch:
                    arrMatch.append(words[i])
                    break
        return arrMatch
