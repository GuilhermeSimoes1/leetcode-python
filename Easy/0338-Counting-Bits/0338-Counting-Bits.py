class Solution:
    def countBits(self, n: int) -> List[int]:
        finalList = []
        for i in range(n+1):
            count = 0
            while i :
                i &= (i-1)
                count += 1
            finalList.append(count)
        return finalList
