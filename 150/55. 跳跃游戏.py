"""

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。


Created at 2023/9/20
"""
from typing import List


class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums)

        # 表示最远能达到的坐标
        dp = [0 for _ in range(n)]

        dp[0] = nums[0]

        for i in range(1, n):
            num = nums[i]

            if dp[i - 1] < i:
                dp[i] = 0
                return False
            else:
                dp[i] = max(dp[i - 1], i + num)

        return True

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        # 表示最远能达到的坐标
        # dp = [0 for _ in range(n)]

        # 由于dp只使用了 dp[i-1] 所以用一个变量保存
        dp = nums[0]

        for i in range(1, n):
            num = nums[i]

            if dp < i:
                return False
            else:
                dp = max(dp, i + num)
        return True


if __name__ == '__main__':
    Solution().canJump([2, 3, 1, 1, 4])
