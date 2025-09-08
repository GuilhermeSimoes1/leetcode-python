class Solution:
    def isPalindrome(self, s: str) -> bool:

        low = s.lower()
        conc = low.replace(' ', '')
        string = ""

        for c in conc:
            if not c.isalnum():
                continue
            else:
                string += c
                continue
        if string == string[::-1]:
            return True
        else:
            return False

sol = Solution()

sol.isPalindrome("0P")