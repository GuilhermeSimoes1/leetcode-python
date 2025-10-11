class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = ""
        finalArray = []

        for i in range(len(digits)):
            num += str(digits[i])

        numInt = int(num) + 1

        for x in str(numInt):
            finalArray.append(int(x))

        return finalArray


