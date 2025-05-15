"""

给你一个字符串 s 和一个 长度相同 的整数数组 indices 。

请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。

返回重新排列后的字符串。

created at 2025/5/15
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = ['' for _ in range(len(s))]

        for idx, ch in enumerate(s):
            arr[indices[idx]] = ch

        return ''.join(arr)
