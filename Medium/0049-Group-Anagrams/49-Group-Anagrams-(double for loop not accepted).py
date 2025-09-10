class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lista = []
        used = set()

        for i in range(len(strs)):
            if strs[i] in used:
                continue

            aux = [strs[i]]
            used.add(strs[i])

            for y in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[y]):
                    aux.append(strs[y])
                    used.add(strs[y])

            lista.append(aux)

        return lista


