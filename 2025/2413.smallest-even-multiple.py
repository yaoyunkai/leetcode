"""
给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。


"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return 2 * n
