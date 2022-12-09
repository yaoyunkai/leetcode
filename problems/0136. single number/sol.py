from functools import reduce
from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        _d = set()

        for n in nums:
            if n in _d:
                _d.remove(n)
            else:
                _d.add(n)

        return _d.pop()

    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    d = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(d))
