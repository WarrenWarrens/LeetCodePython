class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = [ch for ch in s if ch in "aeiouAEIOU"]
        vow.sort()

        res = []
        count = 0
        for ch in s:
            if ch in "aeiouAEIOU":
                res.append(vow[count])
                count += 1
            else:
                res.append(ch)

        s = "".join(res)
        return (s)
