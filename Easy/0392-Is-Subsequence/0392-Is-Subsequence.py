class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        read = 0
        read2 = 0
        count = 0

        while read < len(s) and read2 < len(t):

            letter = s[read]

            while read2 < len(t):

                if t[read2] != letter:
                    read2 += 1
                else:
                    read += 1
                    read2 += 1
                    count += 1
                    break
        if count == len(s):
            return True
        else:
            return False