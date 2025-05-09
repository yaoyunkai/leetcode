"""

给定一个整数 n 。

我们需要根据数字的数位和将 1 到 n 的数字分组。例如，数字 14 和 5 属于 同一 组，而数字 13 和 3 属于 不同 组。

返回最大组的数字数量，即元素数量 最多 的组。


"""


def get_sum(val: int):
    return sum([int(_i) for _i in str(val)])


class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 最大值 9999 -> 36
        _val_list = [0 for _ in range(36)]

        for num in range(1, n + 1):
            _sum = get_sum(num)
            _val_list[_sum - 1] += 1

        return _val_list.count(max(_val_list))


if __name__ == '__main__':
    Solution().countLargestGroup(9999)
