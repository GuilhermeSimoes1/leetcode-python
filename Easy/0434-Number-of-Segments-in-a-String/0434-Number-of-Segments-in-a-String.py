class Solution:
    def countSegments(self, s: str) -> int:

        s = s.strip()

        listaFinal = []

        word = ""
        for l in s:

            if l == " " and word != "":
                listaFinal.append(word)
                word = ""

            elif l != " ":
                word += l

            elif l == " " and word == "":
                continue

        listaFinal.append(word)

        if listaFinal[0] == '':
            return 0

        return len(listaFinal)