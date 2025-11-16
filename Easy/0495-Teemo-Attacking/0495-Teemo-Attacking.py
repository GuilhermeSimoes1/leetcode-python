class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        count = duration

        for i in range(1, len(timeSeries)):

            if timeSeries[i - 1] + duration > timeSeries[i]:
                count += timeSeries[i] - timeSeries[i - 1]
            else:
                count += duration

        return count