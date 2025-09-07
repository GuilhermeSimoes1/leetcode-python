import random
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:

        stack = []
        lastStack = []

        if n == 1:
            return [0]
        if n % 2 != 0:

            lowerPart = int(n / 2)

            for i in range(0,lowerPart):
                numRand = random.randint(-1000,-1)
                stack.append(numRand)

            for y in range(lowerPart,n):
                if not stack:
                    break
                valorPop = stack.pop()
                lastStack.append(valorPop)
                valorAdd = valorPop * (-1)
                lastStack.append(valorAdd)
            lastStack.append(0)
            return lastStack

        else:
            for i in range(0,n//2):
                numRand = random.randint(-1000,-1)
                stack.append(numRand)
                if stack:
                    valorPop = stack.pop()
                    lastStack.append(valorPop)
                    valorAdd = valorPop * (-1)
                    lastStack.append(valorAdd)
            return lastStack
                    


sol = Solution()
print(sol.sumZero(6))