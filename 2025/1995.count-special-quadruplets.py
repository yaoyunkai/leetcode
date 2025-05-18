"""
给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：

nums[a] + nums[b] + nums[c] == nums[d] ，且
a < b < c < d

created at 2025/5/18
"""
from itertools import combinations
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt = 0

        for x1, x2, x3, x4 in combinations(nums, 4):
            if x1 + x2 + x3 == x4:
                cnt += 1
        return cnt


if __name__ == '__main__':
    Solution().countQuadruplets([3, 3, 6, 4, 5])
