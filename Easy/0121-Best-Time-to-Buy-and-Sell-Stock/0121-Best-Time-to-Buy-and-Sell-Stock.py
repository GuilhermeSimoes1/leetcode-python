class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        stackCompra = []
        stackVenda = []
        maxProfit = 0

        for i in range(0, len(prices)):
            if i == 0:
                stackCompra.append(prices[i])
                continue
            if prices[i] < stackCompra[-1] and not stackVenda and i < len(prices) - 1:
                stackCompra.pop()
                stackCompra.append(prices[i])
                continue
            if prices[i] < stackCompra[-1] and stackVenda and i < len(prices) - 1:
                maxProfit = stackVenda[-1] - stackCompra[-1]
                stackCompra.pop()
                stackCompra.append(prices[i])
                stackVenda.pop()
                continue
            if prices[i] > stackCompra[-1] and not stackVenda:
                stackVenda.append(prices[i])
                profit = stackVenda[-1] - stackCompra[-1]
                if maxProfit < profit:
                    maxProfit = profit
                continue
            if prices[i] > stackCompra[-1] and prices[i] > stackVenda[-1]:
                stackVenda.pop()
                stackVenda.append(prices[i])
                profit = stackVenda[-1] - stackCompra[-1]
                if maxProfit < profit:
                    maxProfit = profit
                continue
            if prices[i] > stackCompra[-1] and prices[i] < stackVenda[-1]:
                continue
        return maxProfit

