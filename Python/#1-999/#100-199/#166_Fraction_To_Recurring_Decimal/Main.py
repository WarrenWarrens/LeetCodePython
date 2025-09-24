class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if numerator == 0:
            return "0"

        if numerator * denominator < 0:
            result += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        intresult = numerator // denominator
        result += str(intresult)

        remainder = numerator % denominator
        if remainder == 0:
            return result

        result += "."
        remmap = {}  # remainder -> index in result string

        while remainder != 0:
            if remainder in remmap:
                startindex = remmap[remainder]
                result = result[:startindex] + "(" + result[startindex:] + ")"
                break

            remmap[remainder] = len(result)

            remainder *= 10
            digit = remainder // denominator
            result += str(digit)
            remainder %= denominator

        return result
