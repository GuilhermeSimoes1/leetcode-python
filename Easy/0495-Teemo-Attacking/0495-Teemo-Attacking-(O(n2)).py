class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        Array = []

        for i in range(len(timeSeries)):

            n = 0
            while n < duration:
                n += 1
                Array.append(timeSeries[i] + n)

        finalArray = set(Array)

        return len(finalArray)
