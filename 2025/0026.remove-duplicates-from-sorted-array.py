"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。


输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

[1,1,1,1,1,1]

1 [1,_,_,_,_,_]


"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        prev = 0
        cur = 0

        while cur < len(nums):
            if nums[prev] == nums[cur]:
                cur += 1
            else:
                prev += 1
                nums[prev] = nums[cur]

        return prev + 1


if __name__ == '__main__':
    # Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 1, 3, 4])
