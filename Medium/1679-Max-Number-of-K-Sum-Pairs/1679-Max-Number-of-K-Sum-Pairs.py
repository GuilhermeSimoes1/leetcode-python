class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0

        # 1334

        while left < right:
            res = nums[left] + nums[right]

            if res == k:
                count += 1
                left += 1
                right -= 1

            elif res < k:
                left += 1
            else:
                right -= 1
        return count


