class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        nums.sort()

        duplicado = -1
        falta = -1

        for i in range(len(nums) - 1):

            if nums[i + 1] == nums[i]:
                duplicado = nums[i + 1]

            elif nums[i + 1] > nums[i] + 1:
                falta = nums[i] + 1

        if nums[0] != 1:
            falta = 1
        elif nums[-1] != len(nums):
            falta = len(nums)

        return [duplicado, falta]