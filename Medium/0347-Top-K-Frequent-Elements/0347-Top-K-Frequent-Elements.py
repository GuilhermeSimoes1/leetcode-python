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

