"""


Created at 2023/9/7
"""
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxv = -1

        for s in strs:
            try:
                v = int(s)
            except:
                v = len(s)

            if v > maxv:
                maxv = v

        return maxv
