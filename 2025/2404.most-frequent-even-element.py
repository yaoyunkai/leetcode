"""

给你一个整数数组 nums ，返回出现最频繁的偶数元素。

如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。

"""
from collections import defaultdict
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        tmp = defaultdict(int)

        for n in nums:
            if n % 2 == 0:
                tmp[n] += 1

        if len(tmp) == 0:
            return -1

        max_cnt = max(tmp.values())
        return min(k for k in tmp if tmp[k] == max_cnt)


class Solution2:
    def mostFrequentEven(self, nums: List[int]) -> int:
        tmp = defaultdict(int)
        ans = -1

        for n in nums:
            if n % 2 == 1:
                continue
            tmp[n] += 1
            if tmp[n] > tmp[ans] or (tmp[n] == tmp[ans] and n < ans):
                ans = n
        return ans
