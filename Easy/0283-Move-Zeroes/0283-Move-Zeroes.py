class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        w = 0
        r = 0

        while r < len(nums):
            if nums[r] != 0:
                nums[w] = nums[r]
                w += 1
            r += 1
        for i in range(w, len(nums)):
            nums[i] = 0







