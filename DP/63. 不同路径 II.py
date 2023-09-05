"""
Created at 2023/9/4

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


只有前一个位置为1（可达，只有1种方式） ，当前位置为0（无障碍物）这种情况才能到达该位置，
然后为该位置设 1 （可达，只有1种方式）

该位置是否可达=前一个位置的状态and该位置能否可达 得到能否到达这个位置


"""
import pprint
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        # 到达该位置的方式是1种
        obstacleGrid[0][0] = 1

        # 初始化第一列
        for i in range(1, m):
            obstacleGrid[i][0] = 1 if (obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1) else 0

        # 初始化第一行
        for j in range(1, n):
            obstacleGrid[0][j] = 1 if (obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1) else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    # 如果左边和上边的位置也为0 那么当前位置也是不通的
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[0 for _ in range(4)] for _ in range(3)]
    grid[0][2] = 1
    grid[1][2] = 1
    pprint.pprint(grid)

    Solution().uniquePathsWithObstacles(grid)
