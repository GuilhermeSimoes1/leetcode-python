class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        final = []
        count = 1

        for i in range(len(score)):

            count = 1

            for y in range(len(score)):

                if i != y:

                    if score[i] < score[y]:
                        count += 1

            final.append(count)

        for i in range(len(final)):

            if final[i] == 1:
                final[i] = "Gold Medal"

            elif final[i] == 2:
                final[i] = "Silver Medal"

            elif final[i] == 3:
                final[i] = "Bronze Medal"

            else:
                final[i] = str(final[i])

        return final