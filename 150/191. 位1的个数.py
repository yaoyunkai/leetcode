"""

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

Created at 2023/11/13
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n & 1
            n >>= 1

        return res
