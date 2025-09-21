class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        lenght = len(flowerbed)
        count = 0

        for i in range(lenght):
            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i - 1] == 0)
                right = (i == lenght - 1 or flowerbed[i + 1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    count += 1

        return count >= n
