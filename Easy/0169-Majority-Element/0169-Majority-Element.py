class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        maj = 0
        nTimes = 0

        for x, y in dic.items():
            if y > nTimes:
                maj = x
                nTimes = y

        return maj
