"""
给你一个字符串 s ，请你判断字符串 s 是否存在一个长度为 2 的子字符串，在 s 反转后的字符串中也出现。
如果存在这样的子字符串，返回 true；如果不存在，返回 false 。

created at 2025/5/11
"""


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rs = s[::-1]

        for idx in range(len(s) - 1):
            sub_s = s[idx:idx + 2]

            if sub_s in rs:
                return True

        return False


if __name__ == '__main__':
    Solution().isSubstringPresent("abcd")
