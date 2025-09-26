class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        def helperSum(curr_sum, out_element, in_element):

            return curr_sum - out_element + in_element

        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        left = 0
        right = k - 1

        while right < len(nums)-1:
            left += 1
            right += 1
            curr_sum = helperSum(curr_sum, nums[left - 1], nums[right])
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum / k




