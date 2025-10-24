class Solution:
    def isUgly(self, n: int) -> bool:

        res = n

        if res <= 0:
            return False

        while res % 2 == 0 or res % 3 == 0 or res % 5 == 0:

            if res % 2 == 0:
                res = res // 2

            if res % 3 == 0:
                res = res // 3

            if res % 5 == 0:
                res = res // 5

        if res == 1:
            return True
        else:
            return False