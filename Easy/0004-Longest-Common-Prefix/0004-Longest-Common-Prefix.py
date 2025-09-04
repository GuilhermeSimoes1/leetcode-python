class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        commonLista = []
        delimiter = ""

        for i in range(0, len(strs)):

            if i == 0 and len(strs) == 1:
                onlyOne = strs[i]
                return onlyOne

            elif i == 0 and i + 1 < len(strs):
                for x, y in zip(strs[i], strs[i + 1]):
                    if x == y:
                        commonLista.append(x)
                    else:
                        break

            elif 0 < i < len(strs):
                word = delimiter.join(commonLista)
                commonLista.clear()
                for x, y in zip(word, strs[i]):
                    if x == y:
                        commonLista.append(x)
                    else:
                        break

        word = delimiter.join(commonLista)
        output = word
        print(output)
        return output



