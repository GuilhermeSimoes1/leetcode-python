class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        right = 0
        w = set()

        for right in range(len(nums)):

            if nums[right] in w:
                return True

            w.add(nums[right])

            if len(w) > k:
                w.remove(nums[right - k])

        return False


