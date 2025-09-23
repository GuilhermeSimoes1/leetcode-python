class Solution:
    def reverseWords(self, s: str) -> str:
        auxList = []
        auxList2 = []
        finalList = []
        reverseString = s[::-1]
        word = ""

        for x in s:
            if x != " ":
                word += x
            else:
                auxList.append(word)
                word = ""
        if word:
            auxList.append(word)

        for x in auxList:
            if x != "":
                auxList2.append(x)

        for i in range(len(auxList2) - 1, -1, -1):
            finalList.append(auxList2[i])

        result = " ".join(finalList)

        return result

