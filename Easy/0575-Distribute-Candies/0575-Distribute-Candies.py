class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        count = len(candyType) / 2
        noDuplicates = list(set(candyType))

        if count > len(noDuplicates):
            return int(len(noDuplicates))
        else:
            return int(count)

