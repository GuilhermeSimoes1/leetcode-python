class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        finalList = []

        for i in range(len(gain)):
            if i == 0:
                finalList.append(0)
                finalList.append(gain[i])
            else:
                altitude = gain[i] + finalList[-1]
                finalList.append(altitude)

        finalList.sort()
        highestAltitude = finalList[-1]
        return highestAltitude

