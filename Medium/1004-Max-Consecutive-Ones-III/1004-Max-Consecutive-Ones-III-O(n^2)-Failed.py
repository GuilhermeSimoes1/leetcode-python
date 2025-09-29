class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        maxConsecutive = 0
        left = 0

        while left < len(nums):
            count = 0
            kk = 0

            for i in range(left, len(nums)):
                if nums[i] == 1:
                    count += 1
                elif nums[i] == 0 and kk < k:
                    count += 1
                    kk += 1
                else:
                    break

            maxConsecutive = max(maxConsecutive, count)
            left += 1

        return maxConsecutive
