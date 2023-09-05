"""
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。
之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。


输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。


输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。


Created at 2023/9/5
"""
import pprint
from typing import List


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        转换问题
        将原数组转换为 保存元素个数的数组, 那么相邻的元素不可一起使用
        下标表示 原数组中的元素

        dp[i] = max(dp[i-1], dp[i-2] + i * new_nums[i])

        :param nums:
        :return:
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_item = max(nums)
        new_nums = [0 for _ in range(max_item + 1)]

        for i in nums:
            new_nums[i] += 1

        dp = [0 for _ in range(max_item + 1)]
        # 当 max = 1 的时候，最优解: all[1] * 1
        dp[1] = new_nums[1] * 1

        for i in range(2, max_item + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + new_nums[i] * i)

        return dp[max_item]


if __name__ == '__main__':
    Solution().deleteAndEarn([2, 2, 3, 3, 3, 4])
