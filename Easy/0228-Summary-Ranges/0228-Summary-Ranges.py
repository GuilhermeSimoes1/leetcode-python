class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        finalList = []
        stack = []

        stack = [nums[0]]
        prev = nums[0]

        if len(nums) > 1:

            for i in range(1, len(nums)):

                if prev + 1 == nums[i]:
                    stack.append(nums[i])
                    prev = nums[i]

                else:

                    if len(stack) > 1:
                        finalList.append(f"{stack[0]}->{stack[-1]}")
                        stack.clear()
                        prev = nums[i]
                        stack.append(nums[i])
                    else:

                        finalList.append(f"{stack[0]}")
                        stack.clear()
                        prev = nums[i]
                        stack.append(nums[i])

            if len(stack) > 1:
                finalList.append(f"{stack[0]}->{stack[-1]}")
                stack.clear()
                prev = nums[i]
                stack.append(nums[i])
            else:
                finalList.append(f"{stack[0]}")
                stack.clear()
                prev = nums[i]
                stack.append(nums[i])
        else:
            return [str(nums[0])]
        return finalList


