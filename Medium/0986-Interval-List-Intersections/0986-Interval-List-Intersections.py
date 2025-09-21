class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        if not firstList or not secondList:
            return []

        finalList = []

        for x, y in firstList:
            for xx, yy in secondList:
                if max(x, xx) <= min(y, yy):
                    finalList.append([max(x, xx), min(y, yy)])

        return finalList
