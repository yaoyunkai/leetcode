"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

Created at 2023/9/4
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[n] = dp[n-1] + dp[n-2]

        到 n台阶的前一步是 n-1 或者 n-2

        :param n:
        :return:
        """

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    ret = Solution().climbStairs(5)
    print(ret)
