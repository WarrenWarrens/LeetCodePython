class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        carry = 0
        binaryreturn = []

        maxlen = max(len(a), len(b))
        for i in range(maxlen):
            digita = int(a[i]) if i < len(a) else 0
            digitb = int(b[i]) if i < len(b) else 0

            total = digita + digitb + carry
            binaryreturn.append(str(total % 2))
            carry = total // 2

        if carry:
            binaryreturn.append('1')

        return ''.join(binaryreturn[::-1])