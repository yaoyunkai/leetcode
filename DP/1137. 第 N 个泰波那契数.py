"""
Created at 2023/9/4

泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

"""


class Solution:
    def tribonacci1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0 for _ in range(n + 1)]

        dp[0] = 0
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a = 0
        b = c = 1

        for i in range(3, n + 1):
            c, b, a = a + b + c, c, b

        return c


if __name__ == '__main__':
    Solution().tribonacci(25)
