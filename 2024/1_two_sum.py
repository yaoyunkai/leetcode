"""
nums = [2,7,11,15], target = 9
[0,1]


Created at 2024/7/16
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _tmp_dict = {}

        for idx, num in enumerate(nums):
            if target - num in _tmp_dict:
                return [idx, _tmp_dict[target - num]]

            _tmp_dict[num] = idx

        return []
