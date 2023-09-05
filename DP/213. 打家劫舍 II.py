"""


Created at 2023/9/5
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 点睛：与打家劫舍I的区别是屋子围成了一个环
        #   那么，很明显可以分为三种情况：
        #   1. 首位都不偷
        #   2. 偷首不偷尾
        #   3. 不偷首偷尾
        # 显然，第1种方式损失太大，选取2、3。
        # 那么，分为两种情况，分别计算不包含首和不包含尾这两种情况来判断哪个大哪个小

        # 1.dp[i] 代表当前最大子序和
        # 2.动态方程: dp[i] = max(dp[i-1] and , nums[i-1]+dp[i-2])
        # 3.初始化: 给没有房子时，dp一个位置，即：dp[0]
        #   3.1 当size=0时，没有房子，dp[0]=0；
        #   3.2 当size=1时，有一间房子，偷即可：dp[1]=nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(self.rob_old(nums1), self.rob_old(nums2))

    def rob_old(self, nums: List[int]) -> int:
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
