class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        finalString = ""

        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop()

        for ch in stack:
            finalString += ch
        return finalString
