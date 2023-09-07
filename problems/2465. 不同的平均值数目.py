"""

给你一个下标从 0 开始长度为 偶数 的整数数组 nums 。

只要 nums 不是 空数组，你就重复执行以下步骤：

找到 nums 中的最小值，并删除它。
找到 nums 中的最大值，并删除它。
计算删除两数的平均值。
两数 a 和 b 的 平均值 为 (a + b) / 2 。

比方说，2 和 3 的平均值是 (2 + 3) / 2 = 2.5 。
返回上述过程能得到的 不同 平均值的数目。


Created at 2023/9/7
"""
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg_set = set()

        nums.sort()

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            avg_set.add(nums[lo] + nums[hi])
            lo += 1
            hi -= 1

        return len(avg_set)


if __name__ == '__main__':
    Solution().distinctAverages([4, 1, 4, 0, 3, 5])
