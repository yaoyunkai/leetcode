"""
给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。

created at 2025/5/15
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        arr = []

        for idx in range(len(s), 0, -3):
            # print(idx)
            # print(s[max(0, idx - 3):idx])
            arr.append(s[max(0, idx - 3):idx])

        return '.'.join(arr[::-1])


if __name__ == '__main__':
    ret = Solution().thousandSeparator(1234567819)
    print(ret)
