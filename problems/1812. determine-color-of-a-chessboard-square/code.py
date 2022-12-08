class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        tmp = int(coordinates[1]) + ord(coordinates[0])
        if tmp % 2 == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    demo = 'a1'
    print(ord('a'))
    print(Solution().squareIsWhite('h3'))
