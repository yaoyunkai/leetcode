"""


Created at 2024/7/16
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted(strs)
        print(strs)


if __name__ == '__main__':
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
