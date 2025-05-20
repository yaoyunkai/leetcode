"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_len = 0

        start = 0
        end = 1

        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                max_len = max(max_len, end - start)
                start += 1
                end = start + 1

        return max(max_len, end - start)


if __name__ == '__main__':
    Solution().lengthOfLongestSubstring('pwwkew')
