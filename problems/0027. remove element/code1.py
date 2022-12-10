"""

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

"""
from typing import List


class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        count = 0
        length = len(nums)
        for i in nums:
            if i == val:
                count += 1

        for i in range(count):
            nums.remove(val)

        return length - count

    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        j = 0
        for i, number in enumerate(nums):
            if number != val:
                nums[j] = nums[i]
                j += 1
        return j
