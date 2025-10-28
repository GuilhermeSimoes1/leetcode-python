class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        mul = 1

        while mul < n:
            mul *= 4

        if mul != n:
            return False
        return True