class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        alist = []

        if len(ransomNote) > len(magazine):
            return False
        else:
            for i in magazine:
                alist.append(i)
            for j in ransomNote:
                if j in alist:
                    alist.remove(j)
                else:
                    return False
            return True





