"""
给你一个字符串 num ，表示一个大整数。如果一个整数满足下述所有条件，则认为该整数是一个 优质整数 ：

该整数是 num 的一个长度为 3 的 子字符串 。
该整数由唯一一个数字重复 3 次组成。
以字符串形式返回 最大的优质整数 。如果不存在满足要求的整数，则返回一个空字符串 "" 。

created at 2025/5/11
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        arr = [f'{i}{i}{i}' for i in range(9, -1, -1)]

        for ch in arr:
            if ch in num:
                return ch
        return ''
