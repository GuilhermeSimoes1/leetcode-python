class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carryBit = 1
        newArray = []

        for i in range(len(digits) - 1, -1, -1):

            res = digits[i] + carryBit
            digits[i] = res % 10
            carryBit = res // 10

            if carryBit == 0:
                break

        if carryBit > 0:
            digits.insert(0, carryBit)
        return digits





