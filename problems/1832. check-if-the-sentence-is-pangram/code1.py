class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if not sentence:
            return False

        tmp = [i for i in sentence]
        return len(set(tmp)) == 26


if __name__ == '__main__':
    pass
