class Solution:
    def isValid(self, s: str) -> bool:

        dic = {

            "(": ")",
            "[": "]",
            "{": "}"
        }

        aux = 0
        stack = []

        if len(s) % 2 != 0:
            return False
        for x in s:
            stack.append(x)
        for i in range(0, len(s)):
            for y in range(1, len(s)):
                aux += 1
                if dic[stack[i]] == stack[y] and aux%2 == 0 or aux == 1:
                    aux = 0
                    continue


        return True



sol = Solution()
print(sol.isValid("[]"))