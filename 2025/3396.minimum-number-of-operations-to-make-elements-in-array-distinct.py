"""

给你一个整数数组 nums，你需要确保数组中的元素 互不相同 。为此，你可以执行以下操作任意次：

从数组的开头移除 3 个元素。如果数组中元素少于 3 个，则移除所有剩余元素。
注意：空数组也视作为数组元素互不相同。返回使数组元素互不相同所需的 最少操作次数 。
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0

        while len(set(nums)) != len(nums):
            nums = nums[3:]
            cnt += 1

        return cnt


class Solution2:
    """
    从后看不重复集合

    """

    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()

        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            if x in seen:
                return i // 3 + 1
            seen.add(x)

        return 0
