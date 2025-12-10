class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        finalArray = []

        for i in range(len(list1)):

            for y in range(len(list2)):

                if list1[i] == list2[y]:
                    finalArray.append([i, y])

        minSumm = 1000000000000000

        finalFinalArray = []

        for x, y in finalArray:

            if x + y < minSumm:

                minSumm = x + y

                finalFinalArray = [[x, y]]

            elif x + y == minSumm:

                finalFinalArray.append([x, y])

        ultimateFinalArray = []

        for item in finalFinalArray:
            x = item[0]

            ultimateFinalArray.append(list1[x])

        return ultimateFinalArray
