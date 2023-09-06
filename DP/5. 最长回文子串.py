"""

给你一个字符串 s，找到 s 中最长的回文子串。

输入：s = "babad"
输出："bab"

一个长度严格大于 2 的回文去掉头尾字符以后，剩下的部分依然是回文。

Created at 2023/9/6
"""


class Solution:

    def longestPalindrome1(self, s: str) -> str:
        """
        暴力破解

        :param s:
        :return:
        """
        n = len(s)
        if n < 2:
            return s

        # 保存当前最长回文数的长度
        max_len = 1
        # 开始位置
        begin = 0

        for i in range(n - 1):

            # 扩大长度 从 i ~ i+1 , n-1
            for j in range(i + 1, n):
                width = j - i + 1

                if width > max_len and self.validate(s, i, j):
                    max_len = width
                    begin = i

        return s[begin: begin + max_len]

    def validate(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # 保存当前最长回文数的长度
        max_len = 1
        # 开始位置
        begin = 0

        # 动态数组: 保存 s[i...j] 是否为回文数
        # 由于 s[i..j] 表示 s 的一个子串，因此 i 和 j 的关系是 i <= j，只需要填这张表格对角线以上的部分；
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        # 单个字符一定是回文串，因此把对角线先初始化为 true
        # 根据第 2 步的说明：当 s[i..j] 的长度为 2 时，只需要判断 s[i] 是否等于 s[j]
        for i in range(n):
            dp[i][i] = 1

        # j: 结束位置 i: 起始位置
        for j in range(1, n):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    # 子串长度为2或者3的时候
                    # if j - 1 - (i + 1) + 1 < 2:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]


if __name__ == '__main__':
    s1 = "aacabd"

    Solution().longestPalindrome(s1)
