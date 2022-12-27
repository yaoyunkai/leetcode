class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)

        return '{:b}'.format(int_a + int_b)


if __name__ == '__main__':
    print(Solution().addBinary('1111', '11101'))
