"""
给你一个下标从 0 开始的字符串 s ，该字符串由用户输入。按键变更的定义是：使用与上次使用的按键不同的键。
例如 s = "ab" 表示按键变更一次，而 s = "bBBb" 不存在按键变更。

返回用户输入过程中按键变更的次数。

注意：shift 或 caps lock 等修饰键不计入按键变更，也就是说，如果用户先输入字母 'a' 然后输入字母 'A' ，不算作按键变更。

created at 2025/5/11
"""


class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt = 0

        left = 0
        right = 0

        while right < len(s):
            if s[right].lower() == s[left].lower():
                right += 1
            else:
                cnt += 1
                left = right
                right += 1
        return cnt


if __name__ == '__main__':
    Solution().countKeyChanges('abbbccc')
