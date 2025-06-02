"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

created at 2025/6/2
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [nums[0]]

        for idx in range(1, len(nums)):
            arr.append(arr[idx - 1] + nums[idx])

        return arr
