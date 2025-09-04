class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        numLista = []

        for c in s:
            numNormal = dic[c]
            numLista.append(numNormal)
        finalLista = []

        if len(numLista) == 1:
            return numLista[0]

        else:
            i = 1
            while i < len(numLista):
                if numLista[i-1] > numLista[i]:
                    finalLista.append(numLista[i-1])
                    i += 1
                elif numLista[i-1] < numLista[i]:
                    finalLista.append(numLista[i] - numLista[i-1])
                    i += 2
                else:
                    finalLista.append(numLista[i-1])
                    i += 1

            if numLista[-1] < numLista[-2] or numLista[-1] == numLista[-2]:
                finalLista.append(numLista[-1])

            result = sum(finalLista)
            return result








