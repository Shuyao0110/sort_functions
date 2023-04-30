class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) < 2:
            return nums

        for index in range(1, len(nums)):
            pointer = index
            while pointer > 0 and nums[pointer] < nums[pointer-1]:
                nums[pointer], nums[pointer-1] = nums[pointer-1], nums[pointer]
                pointer -= 1

        return nums
