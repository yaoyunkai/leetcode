"""
给你一个整数数组 nums 。

请你将 nums 中每一个元素都替换为它的各个数位之 和 。

请你返回替换所有元素以后 nums 中的 最小 元素。

"""
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_cnt = -1

        for num in nums:
            tmp = sum([int(i) for i in str(num)])
            if min_cnt == -1:
                min_cnt = tmp
            else:
                min_cnt = min(min_cnt, tmp)

        return min_cnt
