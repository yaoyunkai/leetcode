"""
给你两个只包含 1 到 9 之间数字的数组 nums1 和 nums2 ，每个数组中的元素 互不相同
，请你返回 最小 的数字，两个数组都 至少 包含这个数字的某个数位。

created at 2025/5/18
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        t1 = set(nums1).intersection(set(nums2))
        if t1:
            return min(t1)

        x, y = min(nums1), min(nums2)
        return min(x * 10 + y, y * 10 + x)
