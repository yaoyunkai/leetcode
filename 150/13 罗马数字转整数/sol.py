"""

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。


通常情况下，罗马数字中小的数字在大的数字的右边。
若输入的字符串满足该情况，那么可以将每个字符视作一个单独的值，累加每个字符对应的数值即可。

若存在小的数字在大的数字的左边的情况，根据规则需要减去小的数字。


Created at 2023/8/30
"""


class Solution:
    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            # 当右边值大于左边值时，减去这个值
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value

        return ans

    def romanToInt1(self, s: str) -> int:
        total = 0

        idx = 0
        while idx < len(s):
            # print(s[idx])
            ch = s[idx]
            if ch == 'I':
                if s[idx: idx + 2] == 'IV':
                    total += 4
                    idx += 1
                elif s[idx: idx + 2] == 'IX':
                    total += 9
                    idx += 1
                else:
                    total += 1

            if ch == 'V':
                total += 5

            if ch == 'X':
                if s[idx: idx + 2] == 'XL':
                    total += 40
                    idx += 1
                elif s[idx: idx + 2] == 'XC':
                    total += 90
                    idx += 1
                else:
                    total += 10

            if ch == 'L':
                total += 50

            if ch == 'C':
                if s[idx: idx + 2] == 'CD':
                    total += 400
                    idx += 1
                elif s[idx: idx + 2] == 'CM':
                    total += 900
                    idx += 1
                else:
                    total += 100

            if ch == 'D':
                total += 500
            if ch == 'M':
                total += 1000

            idx += 1

        # print(total)
        return total


if __name__ == '__main__':
    # Solution().romanToInt('III')
    # Solution().romanToInt('IV')
    # Solution().romanToInt('IX')
    # Solution().romanToInt('LVIII')
    # Solution().romanToInt('MCMXCIV')
    pass
