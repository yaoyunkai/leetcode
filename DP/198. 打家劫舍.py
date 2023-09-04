"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

你当前位于K的房子，你可以选择：1、偷 2、不偷。
第一种方案不能偷k-1的房子，所以f(k)=H(k-1)+f(k-2)；
第二种方案可以偷前(k-1)个房子中的任意房子，所以f(k)=f(k-1)，最终小偷在两种方案中做权衡，f(k)=max(H(k-1)+f(k-2),f(k-1))


Created at 2023/9/4
"""
from typing import List


class Solution:

    def rob1(self, nums: List[int]) -> int:
        # 1.dp[i] 代表当前最大子序和
        # 2.动态方程: dp[i] = max(dp[i-1], nums[i-1]+dp[i-2])
        # 3.初始化: 给没有房子时，dp一个位置，即：dp[0]
        #   3.1 当size=0时，没有房子，dp[0]=0；
        #   3.2 当size=1时，有一间房子，偷即可：dp[1]=nums[0]

        n = len(nums)

        if n == 0:
            return 0

        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = nums[0]

        # dp[i] = nums[i-1] + dp[i-2]
        # dp[i] = dp[i-1]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
        return dp[n]

    def rob(self, nums: List[int]) -> int:
        # 依照上面的思路，其实我们用到的数据永远都是dp的dp[i-1]和dp[i-2]两个变量
        # 因此，我们可以使用两个变量来存放前两个状态值
        # 空间使用由O(N) -> O(1)

        n = len(nums)

        if n == 0:
            return 0

        prev = 0
        curr = nums[0]

        for i in range(2, n + 1):
            # prev = max(curr, nums[i - 1] + prev)
            #
            # curr, prev = prev, curr

            prev, curr = curr, max(curr, nums[i - 1] + prev)

        return curr


if __name__ == '__main__':
    Solution().rob([2, 7, 9, 3, 1])
