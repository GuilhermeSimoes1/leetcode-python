class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        finalArray = []
        for i in range(left, right + 1):

            flag = 1
            num = str(i)

            for y in num:
                if int(y) == 0 or int(num) % int(y) != 0:
                    flag = 0
                    break

            if flag != 0:
                finalArray.append(int(num))

        return finalArray
