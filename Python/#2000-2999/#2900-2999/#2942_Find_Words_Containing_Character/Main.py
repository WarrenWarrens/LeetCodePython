class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        pos = []
        count = 0
        for i in words:
            if x in i:
                pos.append(count)
            count += 1
        return pos

