class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        higherArea = 0

        while left < right:

            l = right - left
            h = min(height[left], height[right])
            area = l * h

            if higherArea < area:
                higherArea = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return higherArea



