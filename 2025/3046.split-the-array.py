"""
3046. 分割数组

给你一个长度为 偶数 的整数数组 nums 。你需要将这个数组分割成 nums1 和 nums2 两部分，要求：

nums1.length == nums2.length == nums.length / 2 。
nums1 应包含 互不相同 的元素。
nums2也应包含 互不相同 的元素。

如果能够分割数组就返回 true ，否则返回 false 。

"""

from collections import defaultdict
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        _map = defaultdict(int, )

        for num in nums:
            _map[num] += 1
            if _map[num] > 2:
                return False

        return True


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 4]
    Solution().isPossibleToSplit(nums)
