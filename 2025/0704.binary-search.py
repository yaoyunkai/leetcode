"""

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


created at 2025/5/15
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == '__main__':
    Solution().search([-1, 0, 3, 5, 9, 12], 9)
