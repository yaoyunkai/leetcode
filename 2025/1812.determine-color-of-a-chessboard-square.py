"""
给你一个坐标 coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。

created at 2025/6/2
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a1 = [False, True, False, True, False, True, False, True]
        a2 = [True, False, True, False, True, False, True, False]

        length = ord(coordinates[0:1]) - ord('a')
        num = ord(coordinates[1:2]) - ord('1')

        if length % 2 == 0:
            return a1[num]
        else:
            return a2[num]


if __name__ == '__main__':
    Solution().squareIsWhite('h8')
