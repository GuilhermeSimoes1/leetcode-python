class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        valueHouses = [0] * len(nums)

        valueHouses[0] = nums[0]
        valueHouses[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            valueHouses[i] = max(valueHouses[i - 1], nums[i] + valueHouses[i - 2])

        return valueHouses[-1]
