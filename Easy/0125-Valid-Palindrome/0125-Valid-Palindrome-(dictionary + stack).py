class Solution:
    def isPalindrome(self, s: str) -> bool:

        dic = {
            "a": "a",
            "b": "b",
            "c": "c",
            "d": "d",
            "e": "e",
            "f": "f",
            "g": "g",
            "h": "h",
            "i": "i",
            "j": "j",
            "k": "k",
            "l": "l",
            "m": "m",
            "n": "n",
            "o": "o",
            "p": "p",
            "q": "q",
            "r": "r",
            "s": "s",
            "t": "t",
            "u": "u",
            "v": "v",
            "w": "w",
            "x": "x",
            "y": "y",
            "z": "z",
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        low = s.lower()
        conc = low.replace(' ', '')
        stack = []
        string = ""

        for c in conc:
            if c not in dic:
                continue
            else:
                stack.append(c)
                continue
        for x in stack:
            string += x

        if string == string[::-1]:
            return True
        else:
            return False

sol = Solution()

sol.isPalindrome("0P")