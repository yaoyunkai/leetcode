"""
Created at 2023/8/31
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

输入：a = "1010", b = "1011"
输出："10101"

输入:a = "11", b = "1"
输出："100"

"""


class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        cnt = int(a, 2) + int(b, 2)
        return bin(cnt)[2:]

    def addBinary(self, a: str, b: str) -> str:

        # 补齐
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a

        ans = ""

        # 上一次的进位状态
        up = 0

        for idx in range(len(a) - 1, -1, -1):

            # 当前位置的结果
            tmp = int(a[idx]) + int(b[idx])
            if tmp == 2:
                # 直接反过来用
                ans = str(up) + ans
                up = 1
            elif tmp == 1 and up == 0:
                ans = "1" + ans
                up = 0
            elif tmp == 1 and up == 1:
                ans = "0" + ans
                up = 1
            else:
                ans = str(up) + ans
                up = 0

        if up == 1:
            return str(up) + ans
        return ans


if __name__ == '__main__':
    ret = Solution().addBinary('111001', '11')
