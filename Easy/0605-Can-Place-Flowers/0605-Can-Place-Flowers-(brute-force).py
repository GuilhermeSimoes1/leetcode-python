class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        minusN = n

        if len(flowerbed) == 1 and n == 1:
            if flowerbed[0] == 0:
                return True

        elif len(flowerbed) == 1 and n == 0:

            if flowerbed[0] == 1:
                return True
            elif flowerbed[0] == 0:
                return True

        for i in range(0, len(flowerbed)):

            if i == 0:

                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    minusN -= 1
                    flowerbed[i] = 1

            elif i == len(flowerbed) - 1:

                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    minusN -= 1
                    flowerbed[i] = 1

            elif flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                minusN -= 1
                flowerbed[i] = 1

        if minusN <= 0:
            return True
        else:
            return False