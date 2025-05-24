"""

给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

created at 2025/5/24
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [
            [1],
            [1, 1],
            [1, 2, 1],
        ]

        if rowIndex < 3:
            return arr[rowIndex]

        # 0 - rowIndex
        for idx in range(rowIndex + 1):
            if idx > 2:
                width = idx + 1
                res = []
                prev_res = arr[idx - 1]

                for col in range(width):
                    if col == 0 or col == width - 1:
                        res.append(1)
                    else:
                        res.append(
                            prev_res[col - 1] + prev_res[col]
                        )
                arr.append(res)

        return arr[-1]


if __name__ == '__main__':
    Solution().getRow(5)
