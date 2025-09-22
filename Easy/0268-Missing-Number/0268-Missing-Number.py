class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenght = len(nums)
        count = 0

        nums.sort()

        for i in range(0,lenght):
            if i != nums[i]:
                return i
        return nums[-1] + 1


