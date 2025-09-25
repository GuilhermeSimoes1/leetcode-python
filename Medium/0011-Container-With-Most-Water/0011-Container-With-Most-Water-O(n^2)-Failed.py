class Solution:
    def maxArea(self, height: List[int]) -> int:

        higherArea = 0

        for i in range(len(height)):

            for y in range(len(height)):

                if y != i:

                    comp = abs(y - i)
                    area = comp * min(height[i], height[y])

                    if higherArea < area:
                        higherArea = area

        return higherArea



