class Solution:
    def isHappy(self, n: int) -> bool:

        listDone = []
        soma = 0
        string = str(n)

        while soma != 1:

            soma = 0

            for x in string:
                soma += int(x) ** 2

            if soma in listDone:
                return False
            else:
                listDone.append(soma)
                string = str(soma)

        if int(string) == 1:
            return True
        else:
            return False


