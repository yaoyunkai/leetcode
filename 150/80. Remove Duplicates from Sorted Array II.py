"""
Created at 2023/8/29

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

nums = [0,0,1,1,1,1,2,3,3]

"""
from typing import List


class Solution:

    def removeDuplicates1(self, nums: List[int]) -> int:
        lo = 1
        hi = 2

        while hi < len(nums):
            if nums[hi] == nums[lo] and nums[hi] == nums[lo - 1]:
                hi += 1
            else:
                nums[lo + 1] = nums[hi]
                lo += 1
                hi += 1

        return lo + 1

    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for right in range(2, len(nums)):
            if nums[right] == nums[left] and nums[right] == nums[left - 1]:
                continue

            left += 1
            nums[left] = nums[right]

        return left + 1

    # 扩展至n个元素
    def removeDuplicates2(self, nums: List[int], K: int):
        left = K - 1

        for right in range(K, len(nums)):
            flag = True
            for i in range(K):
                flag *= nums[right] == nums[left - i]

            if flag:
                continue

            left += 1

            nums[left] = nums[right]

        return left + 1


if __name__ == '__main__':
    Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3])
