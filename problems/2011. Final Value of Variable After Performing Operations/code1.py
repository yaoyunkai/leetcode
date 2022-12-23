from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        if not operations:
            return result

        for i in operations:
            if '++' in i:
                result += 1
            if '--' in i:
                result -= 1
        return result


if __name__ == '__main__':
    pass
