"""
整数反转


Created at 2024/6/26
"""


class Solution:
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        y, result = abs(x), 0

        while y != 0:
            result = result * 10 + y % 10  # 结果累加

            if result > self.MAX:
                return 0

            y //= 10  # 取整除赋值运算符

        return result if x > 0 else 0 - result


if __name__ == '__main__':
    print(Solution().reverse(-123))
