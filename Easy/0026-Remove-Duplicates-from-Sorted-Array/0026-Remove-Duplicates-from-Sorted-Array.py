class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        write = 1
        read = 1

        while read < len(nums):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
                read += 1
            else:
                read += 1

        return write













