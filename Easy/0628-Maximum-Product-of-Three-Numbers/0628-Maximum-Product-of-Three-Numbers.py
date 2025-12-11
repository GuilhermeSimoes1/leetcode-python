class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        finalRes = 1

        if len(nums) >= 3:
            res = nums[-3] * nums[-2] * nums[-1]
            res2 = nums[0] * nums[1] * nums[-1]

            finalRes = max(res, res2)

            return finalRes
