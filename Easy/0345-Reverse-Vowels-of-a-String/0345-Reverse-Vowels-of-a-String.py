class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiouAEIOU")
        listVowels = []
        reverseVowels = ""
        count = -1

        for i in s:
            if i in vowels:
                listVowels.append(i)

        for i in s:
            if i in vowels:
                reverseVowels += listVowels[count]
                count -= 1
            else:
                reverseVowels += i
        return reverseVowels




