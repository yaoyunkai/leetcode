"""
给你一个下标从 0 开始的整数数组 nums ，如果 恰好 删除 一个 元素后，数组 严格递增 ，那么请你返回 true ，
否则返回 false 。如果数组本身已经是严格递增的，请你也返回 true 。

数组 nums 是 严格递增 的定义为：对于任意下标的 1 <= i < nums.length 都满足 nums[i - 1] < nums[i] 。


"""
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        pre, cnt = nums[0], 0

        for idx in range(1, len(nums)):
            if nums[idx] <= pre:
                cnt += 1
                if cnt > 1:
                    return False
                if idx > 1 and nums[idx] <= nums[idx - 2]:
                    pre = nums[idx - 1]
                else:
                    pre = nums[idx]
            else:
                pre = nums[idx]

        return cnt <= 1
