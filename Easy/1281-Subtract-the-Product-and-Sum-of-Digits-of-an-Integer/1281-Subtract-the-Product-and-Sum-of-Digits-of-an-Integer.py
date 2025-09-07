class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        stack = []

        for x in str(n):
            stack.append(x)

        prod = 1
        add = 0

        for i in range(0, len(stack)):
            prod *= int(stack[i])
            add += int(stack[i])

        result = prod - add

        return result