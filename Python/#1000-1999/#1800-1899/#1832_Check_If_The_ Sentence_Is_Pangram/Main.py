class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = []
        for i in range(len(sentence)):
            if letters.count(sentence[i]) < 1:
                letters.append(sentence[i])

        if len(letters) != 26:
            return False
        else:
            return True
