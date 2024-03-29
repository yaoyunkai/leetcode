"""
Created at 2023/8/29

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]

"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0

        for num in nums:
            if num != val:
                nums[left] = num
                left += 1

        return left
