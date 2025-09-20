class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        finalList = []
        flag = ""

        for i in range(len(candies)):
            result = candies[i] + extraCandies
            for y in range(len(candies)):
                if y != i:
                    if result >= candies[y]:
                        continue
                    else:
                        flag = "red"
                        break

            if flag != "red":
                finalList.append(True)
            else:
                finalList.append(False)
                flag = ""

        return finalList



    