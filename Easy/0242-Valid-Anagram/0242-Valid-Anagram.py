class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        stack = []

        if len(s) != len(t):
            return False

        for x in s:
            stack.append(x)

        for y in t:
            if y in stack:
                stack.remove(y)

        if len(stack) == 0:
            return True
        else:
            return False


sol = Solution()
sol.isAnagram("anagra","nagaram")