class Solution:
    def reverseBits(self, n: int) -> int:
        binary32 = format(n, '032b')
        strBinary = str(binary32)
        invertedStrBinary = strBinary[::-1]
        decimalValue = int(invertedStrBinary,2)
        return decimalValue


