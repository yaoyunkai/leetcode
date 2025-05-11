"""
给你一个仅由数字 6 和 9 组成的正整数 num。

你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。

请返回你可以得到的最大数字。

1 <= num <= 10^4

created at 2025/5/10
"""


def int_to_digit_list(n):
    return [int(d) for d in str(n)]


def int_to_digit_list_math(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    digits.reverse()
    return digits


class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = int_to_digit_list(num)

        try:
            six_idx = num_str.index(6)
            num_str[six_idx] = 9

            return int(''.join(str(_i) for _i in num_str))

        except:
            return num


class Solution2:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
