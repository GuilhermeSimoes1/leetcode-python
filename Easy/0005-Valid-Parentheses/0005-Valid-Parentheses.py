class Solution:
    def isValid(self, s: str) -> bool:

        dic = {

            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for element in s:
            if element in dic.values():
                stack.append(element)
            elif not stack or dic[element] != stack.pop():
                return False

        return not stack
