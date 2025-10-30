class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        n = 1
        res = 0
        while res < num:
            res = n * n
            n += 1

        if res == num:
            return True
        else:
            return False
