class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(0, len(nums)):
            for y in range(0, len(nums)):
                if nums[i] == nums[y] and i != y:
                    return True
                else:
                    continue
        return False
