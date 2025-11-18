class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        s1 = "qwertyuiop"
        s2 = "asdfghjkl"
        s3 = "zxcvbnm"

        lista = [s1, s2, s3]
        finalLista = []

        for x in words:

            for y in lista:

                flag = True
                for z in x.lower():

                    if z not in y:
                        flag = False
                        break

                if flag:
                    finalLista.append(x)
                    break
        return finalLista
