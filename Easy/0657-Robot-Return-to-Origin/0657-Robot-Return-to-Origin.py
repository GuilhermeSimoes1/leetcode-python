class Solution:
    def judgeCircle(self, moves: str) -> bool:

        numL = 0
        numR = 0
        numU = 0
        numD = 0

        for i in range(len(moves)):
            if moves[i] == "L":
                numL += 1
            elif moves[i] == "R":
                numR += 1
            elif moves[i] == "U":
                numU += 1
            else:
                numD += 1

        if numL == numR and numU == numD:
            return True
        else:
            return False


