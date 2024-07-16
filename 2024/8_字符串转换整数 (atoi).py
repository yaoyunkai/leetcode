"""

"42"
"   -042"
"1337c0d3"
"0-1"
"words and 987"


Created at 2024/6/26
"""
import string
import re


class Solution:
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        res = []

        for c in s:
            if c == ' ':
                if not res:
                    continue
                else:
                    break

            elif c in '+-':
                if not res:
                    res.append(c)
                else:
                    break

            elif c in string.digits:
                res.append(c)

            else:
                break

        print(res)

        if res == ['+'] or res == ['-']:
            return 0

        if not res:
            return 0

        res = ''.join(res)
        res = int(res)

        if res > self.MAX:
            return self.MAX
        if res < self.MIN:
            return self.MIN
        return res

    def myAtoi2(self, s: str) -> int:
        """
        正则表达式

        :param s:
        :return:
        """

        pattern = re.compile(r' *([+-]?\d+)')

        match = pattern.match(s)
        if not match:
            return 0

        ans = int(match.group(1))
        return min(max(ans, -2 ** 31), 2 ** 31 - 1)


if __name__ == '__main__':
    Solution().myAtoi('42')
    Solution().myAtoi('-042')
    Solution().myAtoi('1337c0d3')
    Solution().myAtoi('0-1')
    Solution().myAtoi('words and 987')
    Solution().myAtoi('  +  413')
