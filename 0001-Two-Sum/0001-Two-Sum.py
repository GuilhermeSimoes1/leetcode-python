class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for ii, num2 in enumerate(nums):
                if num + num2 == target and i != ii:
                    return [i, ii]

