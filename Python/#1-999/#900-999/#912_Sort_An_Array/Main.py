class Solution(object):
    def max_heapify(self, nums, heap_size, index):
        left, right = 2 * index + 1, 2 * index + 2
        largest = index
        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right
        if largest != index:
            nums[index], nums[largest] = nums[largest], nums[index]
            self.max_heapify(nums, heap_size, largest)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, i, 0)

        return nums





