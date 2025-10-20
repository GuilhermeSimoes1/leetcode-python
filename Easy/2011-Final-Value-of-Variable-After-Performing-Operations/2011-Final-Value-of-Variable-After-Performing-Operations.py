class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        value = 0

        for x in operations:
            if x == "--X" or x == "X--":
                value += -1

            if x == "X++" or x == "++X":
                value += 1

        return value