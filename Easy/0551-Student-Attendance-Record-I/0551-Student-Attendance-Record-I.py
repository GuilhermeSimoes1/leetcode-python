class Solution:
    def checkRecord(self, s: str) -> bool:

        countA = 0
        countL = 0
        countLFinal = False

        for i in range(len(s)):

            if s[i] != 'L':
                countL = 0

            if s[i] == 'A':
                countA += 1

            if s[i] == 'L':
                countL += 1

            if countL == 3:
                countLFinal = True

        if countA < 2 and countLFinal == False:
            return True
        else:
            return False
