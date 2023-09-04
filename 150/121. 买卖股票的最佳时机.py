"""

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

Created at 2023/8/30
"""
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        max_val = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                tmp = prices[j] - prices[i]
                if tmp > max_val:
                    max_val = tmp

        return max_val

    def maxProfit2(self, prices: List[int]) -> int:

        min_price = float('+inf')
        max_profit = 0

        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        dp = [0 for _ in range(n)]
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)
        return dp[n - 1]


if __name__ == '__main__':
    Solution().maxProfit([7, 1, 5, 3, 6, 4])
    Solution().maxProfit([9, 3, 12, 1, 2, 3])
