class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for x in strs:
            key = "".join(sorted(x))
            dic[key].append(x)

        return list(dic.values())