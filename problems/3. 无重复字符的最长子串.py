"""
Created at 2023/9/6
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

"""


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:
            return 0

        maxn = 0

        for i in range(len(s)):
            _arr = []
            for j in range(i, len(s)):
                if s[j] not in _arr:
                    _arr.append(s[j])
                else:
                    break
            maxn = max(maxn, len(_arr))

        return maxn

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        left = 0
        lookup = set()

        max_len = 0
        cur_len = 0

        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[i])

                left += 1
                cur_len -= 1

            max_len = max(max_len, cur_len)

            lookup.add(s[i])

        return max_len


if __name__ == '__main__':
    Solution().lengthOfLongestSubstring('abcabcbb')
    Solution().lengthOfLongestSubstring('bbbbb')
    Solution().lengthOfLongestSubstring('au')
