class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        sum1 = nums[0] + nums[1]
        sum2 = nums[0] + nums[2]
        sum3 = nums[1] + nums[2]
        if len(nums) == 3:
            if sum1 > nums[2] and sum2 > nums[1] and sum3 > nums[0]:
                if nums[0] == nums[1] == nums[2]:
                    return "equilateral"
                elif nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
                    return "isosceles"
                else:
                    return "scalene"
            else:
                return "none"
        else:
            return "none"
