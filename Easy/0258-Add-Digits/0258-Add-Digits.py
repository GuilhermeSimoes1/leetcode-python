class Solution:
    def addDigits(self, num: int) -> int:

        res = num
        string = str(res)

        while res >= 10:

            string = str(res)
            summ = 0

            for i in range(len(string)):
                summ += int(string[i])

            res = summ

        return res