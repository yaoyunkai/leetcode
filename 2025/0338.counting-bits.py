"""
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数
，返回一个长度为 n + 1 的数组 ans 作为答案。

"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        _tmp = [0, 1, 1, 2, 1, 2]

        arr = [0 for _ in range(n + 1)]

        for idx in range(0, n + 1):
            if idx <= 5:
                arr[idx] = _tmp[idx]
            else:
                arr[idx] = 1 + arr[self.remove_highest_bit(idx)]

        return arr

    def remove_highest_bit(self, n):
        highest_bit = 1 << (n.bit_length() - 1)
        return n - highest_bit


if __name__ == '__main__':
    for i in range(32):
        print(f'{i:02}: {i:016b}')
