"""
Created at 2023/9/5

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                # 移动lo指针
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == '__main__':
    Solution().searchInsert([1, 3, 5, 6], 5)
