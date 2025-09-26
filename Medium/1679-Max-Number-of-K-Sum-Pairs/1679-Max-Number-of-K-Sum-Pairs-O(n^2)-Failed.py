class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        ls = []

        x = 0
        y = 0
        count = 0

        while x < len(nums):

            number = nums[x]
            y = 0

            while y < len(nums):

                if x not in ls and y not in ls and number + nums[y] == k and x != y:
                    count += 1
                    ls.append(x)
                    ls.append(y)
                    break
                y += 1
            x += 1
        return count


