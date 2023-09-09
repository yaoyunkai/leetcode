"""

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1


A x1 + B x2 + C x3 + ... + N xn = amount


Created at 2023/9/9
"""
from typing import List


class Solution:
    res = 10 ** 100

    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return -1

        self.find(coins, amount, 0)

        if self.res == 10 ** 100:
            return -1
        return self.res

    def find(self, coins, amount, count):
        if amount < 0:
            return

        if amount == 0:
            self.res = min(self.res, count)

        for coin in coins:
            self.find(coins, amount - coin, count + 1)


if __name__ == '__main__':
    # Solution().coinChange(coins=[1, 2, 5], amount=11)
    Solution().coinChange(coins=[2], amount=3)
