"""
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非严格递减顺序排列。
请你统计并返回 grid 中 负数 的数目。

"""
from typing import List


class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] >= 0:
                    continue
                else:
                    cnt += (m - j)
                    break

        return cnt


if __name__ == '__main__':
    pass
