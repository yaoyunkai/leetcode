"""

abcabcbb



Created at 2024/7/16
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)

        # rk , 第k个字符不重复子串的结束位置
        rk, ans = -1, 0

        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])

            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1

            ans = max(ans, rk - i + 1)

        return ans

    def lengthOfLongestSubstring1(self, s: str) -> int:
        # 每个index的最大长度
        max_len = 0

        for i in range(len(s)):
            max_len = max(max_len, self._get_len(i, s))

        return max_len

    def _get_len(self, index, s):
        _arr = []

        for i in range(index, len(s)):
            if s[i] not in _arr:
                _arr.append(s[i])
            else:
                break

        return len(_arr)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('lengthOfLongestSubstring'))
