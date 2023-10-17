"""
给你一个正整数 n ，请你计算在 [1，n] 范围内能被 3、5、7 整除的所有整数之和。
返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。


Created at 2023/10/17
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        cnt = 0

        for i in range(1, n + 1):

            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                cnt += i

        return cnt
