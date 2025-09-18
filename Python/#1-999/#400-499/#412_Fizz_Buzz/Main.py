class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for j in range(1, n + 1):
            if j % 3 == 0:
                if j % 5 == 0:
                    list.append("FizzBuzz")
                else:
                    list.append("Fizz")
            elif j % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(j))
        return list

