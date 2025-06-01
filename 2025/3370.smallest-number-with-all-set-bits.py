"""
给你一个正整数 n。

返回 大于等于 n 且二进制表示仅包含 置位 位的 最小 整数 x 。

置位 位指的是二进制表示中值为 1 的位。

created at 2025/6/1
"""


class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        1111


        :param n:
        :return:
        """
        n_bits = n.bit_length()
        cnt = 0

        for i in range(n_bits):
            cnt += 2 ** i
        return cnt


if __name__ == '__main__':
    Solution().smallestNumber(12)
