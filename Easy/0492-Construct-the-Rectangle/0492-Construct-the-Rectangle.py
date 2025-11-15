class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = int(area ** 0.5)
        w = l

        while l * w != area:
            if l * w < area:
                w += 1
            else:
                l -= 1

        return [w, l]
