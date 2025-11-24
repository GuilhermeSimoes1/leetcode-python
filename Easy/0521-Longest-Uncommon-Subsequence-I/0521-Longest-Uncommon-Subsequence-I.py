class Solution:
    def findLUSlength(self, a: str, b: str) -> int:

        count = 0

        if a == b:
            return -1

        if len(a) != len(b):
            return max(len(a), len(b))

        else:
            return len(a)   