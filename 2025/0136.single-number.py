"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

任何数和自己做异或运算，结果为 0，即 a ⊕ a=0 。
任何数和 0 做异或运算，结果还是自己，即 a ⊕ 0= ⊕。
异或运算中，满足交换律和结合律，也就是 a ⊕ b ⊕ a=b ⊕ a ⊕ a=b ⊕(a ⊕ a)=b ⊕ 0=b。


"""
from collections import defaultdict
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _map = defaultdict(int)

        for num in nums:
            _map[num] += 1

        for k, v in _map.items():
            if v == 1:
                return k


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
