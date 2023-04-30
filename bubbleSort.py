class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) < 2:
            return nums

        for time in range(len(nums)-1):
            for index in range(0, len(nums)-time-1):
                if nums[index] > nums[index+1]:
                    nums[index], nums[index+1] = nums[index+1], nums[index]

        return nums


my_solution = Solution()
print(my_solution.sortArray([3, 2, 1, 5]))
