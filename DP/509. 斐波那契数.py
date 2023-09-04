"""


Created at 2023/8/31
"""


class Solution:
    def fib1(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = a + b, a
        return a

    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    Solution().fib(10)
