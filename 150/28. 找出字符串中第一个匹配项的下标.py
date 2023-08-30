"""
Created at 2023/8/30

给你两个字符串 haystack 和 needle ，
请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

"""


class Solution:

    def strStr1(self, haystack: str, needle: str) -> int:
        res = -1
        needle_f = needle[0]
        needle_len = len(needle)
        haystack_len = len(haystack)

        for i in range(haystack_len):
            # 不用考虑越界问题, slice 不会越界
            if haystack[i] == needle_f and haystack[i: i + needle_len] == needle:
                res = i
                break
        return res

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        n = len(needle)

        left = 0

        while left < len(haystack):
            if haystack[left] == needle[0]:
                for i in range(1, n):
                    if left + i == len(haystack):
                        return -1
                    if haystack[left + i] != needle[i]:
                        break
                else:
                    return left

            left += 1

        return -1


if __name__ == '__main__':
    ret = Solution().strStr(haystack="sadbutsad", needle="uts")
    ret = Solution().strStr(haystack="leetcode", needle="leeto")
