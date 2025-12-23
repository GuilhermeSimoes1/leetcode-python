class Solution:
    def calPoints(self, operations: List[str]) -> int:

        finalArray = []

        for x in operations:
            if x == "C" and finalArray:
                finalArray.pop()

            elif x == "D" and finalArray:
                finalArray.append(finalArray[-1] * 2)

            elif x == "+" and len(finalArray) >= 2:
                finalArray.append(finalArray[-1] + finalArray[-2])
            else:
                finalArray.append(int(x))

        somaFinal = sum(finalArray)
        return somaFinal