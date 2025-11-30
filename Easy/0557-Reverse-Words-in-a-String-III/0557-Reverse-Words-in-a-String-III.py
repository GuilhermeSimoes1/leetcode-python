class Solution:
    def reverseWords(self, s: str) -> str:

        lista = []
        word = ""

        for i in range(len(s)):

            if s[i] != " ":
                word += s[i]
            else:
                lista.append(word)
                word = ""

        lista.append(word)

        for y in range(len(lista)):
            word = lista[y]

            word = word[::-1]

            lista[y] = word

        finalString = " ".join(lista)
        return finalString






