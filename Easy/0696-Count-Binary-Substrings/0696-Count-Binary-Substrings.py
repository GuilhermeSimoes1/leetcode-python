class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        timesArray = []

        count = 1

        prev = s[0]

        for x in range(1, len(s)):

            if s[x] == prev:

                count += 1

            else:

                timesArray.append(count)
                count = 1
                prev = s[x]

        timesArray.append(count)

        soma = 0

        for i in range(0, len(timesArray) - 1):
            soma += min(timesArray[i], timesArray[i + 1])

        return soma





