class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            left = 0
            right = 0

            for y in range(len(nums)):

                if i == y:
                    continue
                if y < i:
                    left += nums[y]
                else:
                    right += nums[y]

            if left == right:
                return i
        return -1


