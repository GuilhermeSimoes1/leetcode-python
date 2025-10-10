class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0

        stack = []
        indice = 0

        while indice < len(haystack):

            if indice + len(needle) > len(haystack):
                break

            if haystack[indice] == needle[0]:
                stack.append(indice)
                word = ""
                for i in range(indice, indice + len(needle)):
                    word += haystack[i]

                if word == needle:
                    return stack[0]
                else:
                    stack.pop()

            indice += 1
        return -1
