from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                return digits

        tmp = [0 for i in range(n + 1)]
        tmp[0] = 1
        return tmp


if __name__ == '__main__':
    Solution().plusOne([3, 4, 5, 6])
