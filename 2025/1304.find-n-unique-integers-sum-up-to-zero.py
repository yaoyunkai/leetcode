"""
给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。

created at 2025/6/1
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        h = n // 2

        for i in range(1, h + 1):
            arr.append(i)
            arr.append(i * -1)

        if 2 * h < n:
            arr.append(0)

        # print(arr)
        return arr
