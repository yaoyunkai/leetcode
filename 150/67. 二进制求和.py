"""
Created at 2023/8/31
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

输入：a = "1010", b = "1011"
输出："10101"

输入:a = "11", b = "1"
输出："100"

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        cnt = int(a, 2) + int(b, 2)
        return bin(cnt)[2:]


if __name__ == '__main__':
    ret = Solution().addBinary('111', '1111')
    print(ret)
