class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        currNum = 0
        currString = ""

        dic = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        for x in s:
            if x in dic:
                currNum = currNum * 10 + int(x)

            elif x == "[":
                stack.append((currString, currNum))
                currString = ""
                currNum = 0

            elif x == "]":
                prevString, num = stack.pop()
                currString = prevString + num * currString

            else:
                currString += x
        return currString



