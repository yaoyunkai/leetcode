"""

给你一个正整数 n 。n 中的每一位数字都会按下述规则分配一个符号：

最高有效位 上的数字分配到 正 号。
剩余每位上数字的符号都与其相邻数字相反。
返回所有数字及其对应符号的和。

"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n_str = str(n)
        cnt = 0
        flag = True
        for i in n_str:
            if flag:
                cnt += 1 * int(i)
                flag = False
            else:
                cnt += (-1) * int(i)
                flag = True

        return cnt


if __name__ == '__main__':
    ret = Solution().alternateDigitSum(886996)
    print(ret)
