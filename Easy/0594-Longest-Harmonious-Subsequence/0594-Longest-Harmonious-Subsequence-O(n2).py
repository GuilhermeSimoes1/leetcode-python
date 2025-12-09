class Solution:
    def findLHS(self, nums: List[int]) -> int:
        subMaxFinal = 0


        numsUnique = list(set(nums))

        if len(numsUnique) == 1:
            return 0

        for i in range(len(nums)):
            subUp = 0
            subDown = 0
            countX = 0
            for y in range(len(nums)):

                if nums[y] == nums[i]:
                    countX += 1
                elif nums[y] == nums[i] + 1:
                    subUp += 1
                elif nums[y] == nums[i] - 1:
                    subDown += 1

            if subUp > 0:
                subMaxFinal = max(subMaxFinal, countX + subUp)

            if subDown > 0:
                subMaxFinal = max(subMaxFinal, countX + subDown)

        return subMaxFinal