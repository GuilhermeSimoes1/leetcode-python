class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        finalList = []
        for numPass, kmI, kmF in trips:
            finalList.append((kmI, numPass))
            finalList.append((kmF, -numPass))

        finalList.sort()
        current = 0
        for _, nPass in finalList:
            current += nPass
            if current > capacity:
                return False
        return True






