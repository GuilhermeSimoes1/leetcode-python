class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')
        second = float('inf')

        for i in range(0, len(nums)):
            if nums[i] < first:
                first = nums[i]
            if first < nums[i] < second:
                second = nums[i]
            if nums[i] > second:
                return True
        return False






