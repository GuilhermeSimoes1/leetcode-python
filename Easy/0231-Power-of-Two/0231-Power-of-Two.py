class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        value = 0
        i = 0

        while value <= n:

            value = 2 ** i

            if value == n:
                return True
            else:
                i += 1

        return False

