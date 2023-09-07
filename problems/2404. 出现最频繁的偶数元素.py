"""

给你一个整数数组 nums ，返回出现最频繁的偶数元素。

如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。

Created at 2023/9/7
"""
import collections
from typing import List


class Solution:
    def mostFrequentEven1(self, nums: List[int]) -> int:
        max_item = max(nums)

        arr = [0 for _ in range(max_item + 1)]

        for num in nums:
            if num % 2 == 0:
                arr[num] += 1

        tmp = max_item

        for i in range(max_item, -1, -1):
            if arr[i] > arr[tmp]:
                tmp = i

        return tmp if arr[tmp] else -1

    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = collections.Counter(x for x in nums if x % 2 == 0)

        ans, mx = -1, 0

        for x, v in cnt.items():
            if v > mx or (v == mx and ans > x):
                ans, mx = x, v
        return ans


if __name__ == '__main__':
    Solution().mostFrequentEven([4, 4, 4, 9, 2, 4])
