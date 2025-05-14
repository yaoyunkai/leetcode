"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。


"""


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            # print(f'{mid}*{mid}={mid * mid}')
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == '__main__':
    ret = Solution().mySqrt(199999)
    print(ret)
