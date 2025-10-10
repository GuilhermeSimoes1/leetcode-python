class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):

            if nums[i] > target:
                return i
                break
            if nums[i] == target:
                return i
            if i == len(nums) - 1 and nums[i] < target:
                return i + 1
