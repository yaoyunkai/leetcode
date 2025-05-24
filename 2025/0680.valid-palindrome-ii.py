"""
给你一个字符串 s，最多 可以从中删除一个字符。

请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。

created at 2025/5/24
"""


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strPart(s, left)) or isPalindrome(strPart(s, right))
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    Solution().validPalindrome('salhdfoqwhef')
