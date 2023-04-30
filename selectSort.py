class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) < 2:
            return nums

        for index in range(0, len(nums)-1):
            min = index
            for point in range(index+1, len(nums)):
                if nums[min] > nums[point]:
                    min = point
            # self.swap(nums[min],nums[index])
            nums[min], nums[index] = nums[index], nums[min]

        return nums

    # def swap(self,num1,num2):
    #     temp=num2
    #     num2=num1
    #     num1=temp


my_solution = Solution()
print(my_solution.sortArray([3, 2, 1, 5]))
