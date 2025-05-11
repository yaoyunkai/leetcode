"""
给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。


created at 2025/5/11
"""
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        for idx in range(len(arr) - 2):
            num1 = arr[idx]
            num2 = arr[idx + 1]
            num3 = arr[idx + 2]

            if num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1:
                return True

        return False
