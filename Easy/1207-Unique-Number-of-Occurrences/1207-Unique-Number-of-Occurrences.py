class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dic = {}

        for i in range(len(arr)):
            try:
                dic[arr[i]] += 1
            except:
                dic[arr[i]] = 1

        values = list(dic.values())

        if len(values) == len(set(values)):
            return True
        else:
            return False






