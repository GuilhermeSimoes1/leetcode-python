from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int],k) -> List[int]:
        dic = defaultdict(int)
        listaTop = []
        finalList = []

        for x in nums:
            key = x
            dic[key] += 1

        for i in sorted(dic, key=dic.get, reverse=True):
            listaTop.append(i)

        for i in range(0,k):
            finalList.append(listaTop[i])

        return finalList







solution = Solution()
print(solution.topKFrequent([1,2,3,3,5,6,6,6,7],2))