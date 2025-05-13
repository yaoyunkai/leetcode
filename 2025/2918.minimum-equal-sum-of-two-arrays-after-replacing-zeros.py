"""
给你两个由正整数和 0 组成的数组 nums1 和 nums2 。

你必须将两个数组中的 所有 0 替换为 严格 正整数，并且满足两个数组中所有元素的和 相等 。

返回 最小 相等和 ，如果无法使两数组相等，则返回 -1 。

=====================================



"""
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        sum_1 + (n) = sum_2 + (n)

        :param nums1:
        :param nums2:
        :return:
        """

        s1 = sum(max(x, 1) for x in nums1)
        s2 = sum(max(x, 1) for x in nums2)

        if s1 < s2 and 0 not in nums1 or s2 < s1 and 0 not in nums2:
            return -1

        return max(s1, s2)
