class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        stri = str(n)
        prod = 1
        add = 0

        for x in stri:
            prod *= int(x)
            add += int(x)

        result = prod - add
        return result