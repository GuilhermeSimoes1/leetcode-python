class Solution:
    def findLHS(self, nums: List[int]) -> int:

        numsTimes = {}

        for n in nums:
            if n not in numsTimes:
                numsTimes[n] = 0
            numsTimes[n] += 1

        maxSub = 0

        for x in numsTimes:

            if x + 1 in numsTimes:
                maxSub = max(maxSub, numsTimes[x] + numsTimes[x + 1])

        return maxSub