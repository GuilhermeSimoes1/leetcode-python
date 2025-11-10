class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        count = 0

        g.sort()
        s.sort()
        flag = "n"

        for x in g:

            for y in s:

                if x <= y:
                    count += 1
                    flag = "s"
                    s.remove(y)
                    break
                else:
                    flag = "n"

            if flag == "n":
                return count

        return count