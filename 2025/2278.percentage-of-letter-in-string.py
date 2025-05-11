"""
给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。

created at 2025/5/11
"""
import math


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        s_len = len(s)

        for c in s:
            if letter == c:
                cnt += 1

        return math.floor(cnt * 100 / s_len)
