"""

在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]

Created at 2023/9/6
"""
from typing import List


class Solution:
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        result = 0

        # 当只有一行时，只要有1 面积就是1
        if row == 1:
            return int(max(matrix[0]))

        # dp[i][j] 表示以当前点为右下角的正方形的最大边长
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for i in range(row):
            for j in range(col):
                # 当给dp左边和上边套了一排0之后, matrix[i][j]的位置和dp[i + 1][j + 1]一致
                if matrix[i][j] == "1":
                    # 取 左 左上 上 最小的边长来计算当前点的最长边长
                    dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j], dp[i][j + 1])
                    result = max(result, dp[i + 1][j + 1] * dp[i + 1][j + 1])

        return result

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        result = 0

        # 当只有一行时，只要有1 面积就是1
        if row == 1:
            return int(max(matrix[0]))

        # dp[j] 一维数组
        dp = [0 for _ in range(col + 1)]

        for rows in matrix:
            # 左上角 第一次永远是0
            # 理解 north_west的赋值情况
            north_west = 0
            for j in range(col):

                # 从1开始 等于上一次的结果
                new_north_west = dp[j + 1]
                if rows[j] == '1':
                    # dp[j] 左边的值
                    # dp[j+1] 上边的值
                    dp[j + 1] = 1 + min(dp[j], dp[j + 1], north_west)
                    result = max(result, dp[j + 1])

                else:
                    dp[j + 1] = 0

                north_west = new_north_west

        return result * result


if __name__ == '__main__':
    arr = [["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "1", "1", "1"]]

    arr2 = [["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"]]
    Solution().maximalSquare(arr2)
