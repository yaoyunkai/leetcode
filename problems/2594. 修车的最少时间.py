"""

给你一个整数数组 ranks ，表示一些机械工的 能力值 。
ranks[i] 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。

同时给你一个整数 cars ，表示总共需要修理的汽车数目。

输入：ranks = [4,2,3,1], cars = 10
输出：16
解释：
- 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
- 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
- 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
- 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。


Created at 2023/9/7
"""
from typing import List
from math import isqrt


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0

        # 让能力值最低（修车最快）的人修好所有车所需要的时间。
        right = min(ranks) * cars * cars

        while left + 1 < right:
            mid = left + (right - left) // 2
            if sum(isqrt(mid // r) for r in ranks) >= cars:
                right = mid
            else:
                left = mid

        return right
