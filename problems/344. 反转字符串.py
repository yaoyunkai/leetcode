"""
Created at 2023/9/3

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(0, n):
            if i == n // 2:
                break

            s[i], s[n - i - 1] = s[n - i - 1], s[i]
