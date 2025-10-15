class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}

        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1

        for key, value in dic.items():
            if value == 1:
                return key
