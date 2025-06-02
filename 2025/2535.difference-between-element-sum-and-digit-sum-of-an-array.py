"""
给你一个正整数数组 nums 。

元素和 是 nums 中的所有元素相加求和。
数字和 是 nums 中每一个元素的每一数位（重复数位需多次求和）相加求和。
返回 元素和 与 数字和 的绝对差。

created at 2025/6/2
"""
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0

        for num in nums:
            sum1 += num
            sum2 += sum(int(i) for i in str(num))

        return abs(sum1 - sum2)
