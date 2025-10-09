class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        write = 0
        read = 0

        while read < len(nums):

            if nums[read] != val:
                nums[write] = nums[read]
                read += 1
                write += 1
            else:
                read += 1
        return write



