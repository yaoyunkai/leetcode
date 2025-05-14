"""
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

"""
from typing import List


class Solution:

    def add(self, set_, value):
        if value == '.':
            return True
        if value in set_:
            return False
        else:
            set_.add(value)
            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tmp_x = set()
        tmp_y = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }
        tmp_box = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if not self.add(tmp_x, cell):
                    return False
                if not self.add(tmp_y[j], cell):
                    return False
                box_idx = (i // 3) * 3 + (j // 3)
                if not self.add(tmp_box[box_idx], cell):
                    return False
            tmp_x = set()
        return True


if __name__ == '__main__':
    demo1 = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "6", ".", ".", ".", "."],
             ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
             [".", ".", ".", "7", ".", ".", ".", ".", "."],
             [".", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    Solution().isValidSudoku(demo1)
