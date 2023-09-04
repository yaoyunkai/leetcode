"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。


Created at 2023/9/4
"""
import pprint


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """

        M 表示为行
        N 表示为列

        dp[i][j]: 代表到达位置 (i, j) 的所有路径的总数

        想要到达位置(i, j)，可以从位置(i-1, j)或者(i, j-1)出发到达。
        到达位置(i, j) 的总的路径数一定是 到达位置(i-1, j)路径数 + 到达位置(i, j-1)路径数
        动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]

        初始值:
        在机器人走第 0 行，第 0 列的时候，无论怎么走，都只有 1 种走法。
        因此，初始化值的设定，一定是 dp[0...m][0] 或者 dp[0][0...n] 都等于1

        :param m:
        :param n:
        :return:
        """

        # dp[i][j]: 代表到达位置 (i, j) 的所有路径的总数
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # pprint.pprint(dp)

        for j in range(n):
            dp[0][j] = 1

        for i in range(m):
            dp[i][0] = 1

        # pprint.pprint(dp)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        pprint.pprint(dp)
        return dp[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        """
        每一步骤中的状态值只与左边相邻的值和上面的值相关
        优化空间: 只使用了左边和上边两个位置
        
        :param m: 
        :param n: 
        :return: 
        """
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]


if __name__ == '__main__':
    Solution().uniquePaths2(3, 7)
