class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        aux = 0
        nums.append(0)

        for i in range(len(nums)):
            if nums[i] == 1:
                aux += 1

            if nums[i] == 0:
                count = max(count, aux)
                aux = 0

        return count