"""

示例 1：

输入：s = "the sky is blue"
输出："blue is sky the"
示例 2：

输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。
示例 3：

输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。

Created at 2023/9/12
"""


class Solution:
    def reverseWords1(self, s: str) -> str:
        res = s.split()
        res.reverse()
        return ' '.join(res)

    def reverseWords(self, s: str) -> str:
        s = s.strip()

        i = j = len(s) - 1
        res = []

        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i + 1:j + 1])

            while i >= 0 and s[i] == " ":
                i -= 1
            j = i

        return ' '.join(res)


if __name__ == '__main__':
    print("  hello world  ".split())
    print("a good   example".split())

    Solution().reverseWords("a good   example")
