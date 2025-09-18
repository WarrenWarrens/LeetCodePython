class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowbank = []
        cosbank = []
        vowcount = 0
        coscount = 0

        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                vowbank.append(s[i])
            else:
                cosbank.append(s[i])

        for i in range(len(vowbank)):
            if vowbank.count(vowbank[i]) > vowcount:
                vowcount = vowbank.count(vowbank[i])

        for j in range(len(cosbank)):
            if cosbank.count(cosbank[j]) > coscount:
                coscount = cosbank.count(cosbank[j])

        return vowcount + coscount