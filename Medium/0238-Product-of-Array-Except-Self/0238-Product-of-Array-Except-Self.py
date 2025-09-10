class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []
        final = []

        value = 1

        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                value *= nums[i - 1]
                prefix.append(value)
        print(prefix)

        value = 1

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                suffix.append(1)
            else:
                value *= nums[i + 1]
                suffix.insert(0, value)
        print(suffix)


        for x,y in zip(prefix, suffix):
            final.append(x * y)
        print(final)
        return final
