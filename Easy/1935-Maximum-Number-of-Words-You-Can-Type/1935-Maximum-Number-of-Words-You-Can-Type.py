class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        array = []
        count = 0
        word = ""
        aux = ""

        text += " "

        for i in range(0, len(text)):
            word += text[i]

            if text[i] == " ":
                for y in brokenLetters:
                    if y in word:
                        word = ""
                        aux = "yes"
                        break

                if aux == "":
                    count += 1

                elif aux == "yes":
                    aux = ""
                    continue

        return count
