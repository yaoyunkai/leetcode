"""

给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。


输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。


2
3  4
6  5  7
4  1  8  3

dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + nums[i][j]


Created at 2023/9/5
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)

        if height == 1:
            return triangle[0][0]

        for i in range(1, height):
            # 第 i 层的列表和层数相等
            for j in range(i + 1):
                # 第0列时,没有更左边的
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                # 最后一列, 只有左上方有数据
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                # 不是第一个不是最后一个, 在上方或者左上方取最小
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])

        # 最后一层最小的为结果
        return min(triangle[-1])


if __name__ == '__main__':
    arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    Solution().minimumTotal(triangle=arr)
