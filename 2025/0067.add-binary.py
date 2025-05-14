class Solution:
    def addBinary(self, a: str, b: str) -> str:
        cnt = int(a, 2) + int(b, 2)
        return f'{cnt:b}'


if __name__ == '__main__':
    print(Solution().addBinary('1000', '10'))
