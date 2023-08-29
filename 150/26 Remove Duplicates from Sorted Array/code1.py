"""
Created at 2023/8/29
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，
使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        小于lo的都是已经排序的
        等于lo的正在比较的
        
        
        :param nums: 
        :return: 
        """
        lo = 0
        hi = 1

        while hi < len(nums):
            if nums[lo] == nums[hi]:
                hi += 1
            else:
                nums[lo + 1] = nums[hi]
                lo += 1
                hi += 1

        return lo + 1


if __name__ == '__main__':
    Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
