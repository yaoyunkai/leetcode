"""
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        mm = dict()

        for ch in s:
            mm[ch] = not ch in mm

        for idx, ch in enumerate(s):
            if mm[ch]:
                return idx
        return -1
