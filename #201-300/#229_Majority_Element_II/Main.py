#Not happy with this one
class Solution(object):
    def BoyerMoore(self, nums):
        if not nums:
            return []

        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        n = len(nums)
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 is not None and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.BoyerMoore(nums)

