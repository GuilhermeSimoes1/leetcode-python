class Solution:
    def mySqrt(self, x: int) -> int:

        z = 1

        while z*z <= x:
            if z*z == x:
                return z
            z += 1
        return z-1