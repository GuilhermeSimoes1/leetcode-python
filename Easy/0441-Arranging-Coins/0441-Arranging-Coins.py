class Solution:
    def arrangeCoins(self, n: int) -> int:

        count = 0
        escadas = 0
        while n >= 0:
            count += 1
            n -= count
            if n >= 0:
                escadas += 1
            else:
                return escadas

        return escadas


