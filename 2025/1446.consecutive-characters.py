"""
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串 s 的 能量。

输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。


created at 2025/5/10
"""


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1

        cnt = 0
        prev = 0
        cur = 0

        while cur < len(s):
            if s[prev] == s[cur]:
                cur += 1
            else:
                cnt = max(cur - prev, cnt)
                prev = cur

        return max(cur - prev, cnt)


if __name__ == '__main__':
    Solution().maxPower('cc')
