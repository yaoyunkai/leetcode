"""
给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 k ，
请你返回满足 0 <= i < j < n ，nums[i] == nums[j] 且 (i * j) 能被 k 整除的数对 (i, j) 的 数目 。

输入：nums = [3,1,2,2,2,1,3], k = 2
输出：4
解释：
总共有 4 对数符合所有要求：
- nums[0] == nums[6] 且 0 * 6 == 0 ，能被 2 整除。
- nums[2] == nums[3] 且 2 * 3 == 6 ，能被 2 整除。
- nums[2] == nums[4] 且 2 * 4 == 8 ，能被 2 整除。
- nums[3] == nums[4] 且 3 * 4 == 12 ，能被 2 整除。


created at 2025/5/24
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    Solution().countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2)
