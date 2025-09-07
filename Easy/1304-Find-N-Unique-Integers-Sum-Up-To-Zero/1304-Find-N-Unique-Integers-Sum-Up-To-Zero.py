from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:

        stack = []

        if n == 1:
            return [0]

        if n % 2 == 0:
            for i in range(1,n//2+1):
                stack.append(i)
                stack.append(-i)
            return stack
        else:
            for i in range(1,n//2+1):
                stack.append(i)
                stack.append(-i)
            stack.append(0)
            return stack




