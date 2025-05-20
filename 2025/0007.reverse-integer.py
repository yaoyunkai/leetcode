"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。


"""


class Solution:
    def reverse(self, x: int) -> int:
        arr = []
        neg = x < 0
        cnt = 0
        ret = 0
        x = abs(x)

        while x != 0:
            x, y = divmod(x, 10)
            arr.append(y)
            cnt += 1

        for i in range(cnt):
            ret += arr[i] * (10 ** (cnt - 1 - i))

        if ret > 2 ** 31 - 1:
            return 0

        return -1 * ret if neg else ret


if __name__ == '__main__':
    Solution().reverse(123)
