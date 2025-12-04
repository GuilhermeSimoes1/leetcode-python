class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0

        nums.sort()
        print(nums)

        for i in range(0, len(nums), 2):
            res += min(nums[i], nums[i + 1])

        return res