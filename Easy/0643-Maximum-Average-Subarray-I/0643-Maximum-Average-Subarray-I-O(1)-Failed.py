class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        def helperAvg(left, right, k, lista):

            summ = 0
            for x in range(left, right + 1):
                summ += lista[x]

            return summ/k

        left = 0
        right = k - 1
        greaterAvg = float("-inf")

        while right < len(nums):

            avg = helperAvg(left, right, k, nums)
            if avg > greaterAvg:
                greaterAvg = avg
            left += 1
            right += 1
        return greaterAvg




