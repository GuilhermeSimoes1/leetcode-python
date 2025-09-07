class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        maxNumber = num + t
        x = maxNumber + t
        return x