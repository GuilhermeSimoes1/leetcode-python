class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        dis = []

        for i in range(len(nums)):
            val = abs(nums[i])
            nums[val - 1] = -abs(nums[val - 1])

        for i in range(len(nums)):
            if nums[i] > 0:
                dis.append(i + 1)

        return dis