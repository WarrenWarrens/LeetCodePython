class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        counter = 0
        for i in words:
            if len(i) >= len(pref):
                match = True
                for k in range(len(pref)):
                    if i[k] != pref[k]:
                        match = False
                        break
                if match:
                    counter += 1
        return counter
