class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        salary.pop(len(salary) -1)
        salary.pop(0)
        rvalue = sum(salary) / float(len(salary))
        return rvalue