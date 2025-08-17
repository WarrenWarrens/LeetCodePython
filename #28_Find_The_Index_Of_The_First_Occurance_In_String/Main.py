class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for x in range(len(haystack) - len(needle) + 1):
            if haystack[x] == needle[0]:
                match = True
                for y in range(len(needle)):
                    if needle[y] != haystack[x + y]:
                        match = False
                        break
                if match:
                    return x
        return -1


