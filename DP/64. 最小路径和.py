"""

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

Created at 2023/9/5
"""
from typing import List


class Solution:
    def minPathSum1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 动态数组二维
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        # 初始化dp数组 第一列和第一行
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]

        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        # pprint.pprint(dp)

        for i in range(1, m):
            for j in range(1, n):
                # 状态转移:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        利用现有数组

        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    Solution().minPathSum(grid1)
