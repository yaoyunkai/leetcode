"""

多数元素：

排序取中间值

使用集合


Created at 2023/8/30
"""
import collections

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        # return max(counts.keys(), key=counts.get)
        # print(counts)
        return max(counts.keys(), key=counts.get)


if __name__ == '__main__':
    ret = Solution().majorityElement(nums=[2, 2, 1, 1, 1, 2, 2, 1, 1])
    print(ret)
