"""
返回数组 nums 中 严格递增 或 严格递减 的最长非空子数组的长度。

示例 1：

输入：nums = [1,4,3,3,2]

输出：2

解释：

nums 中严格递增的子数组有[1]、[2]、[3]、[3]、[4] 以及 [1,4] 。

nums 中严格递减的子数组有[1]、[2]、[3]、[3]、[4]、[3,2] 以及 [4,3] 。

因此，返回 2 。

created at 2025/6/2
"""
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cnt = 1
        up = 1
        down = 1

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                up += 1
                down = 1
            elif nums[idx] < nums[idx - 1]:
                up = 1
                down += 1
            else:
                down = 1
                up = 1
            cnt = max(cnt, up, down)

        return cnt


if __name__ == '__main__':
    Solution().longestMonotonicSubarray([1, 4, 3, 3, 2])
