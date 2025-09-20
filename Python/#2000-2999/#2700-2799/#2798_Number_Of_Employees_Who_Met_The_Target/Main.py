class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        met = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                met += 1
        return met
