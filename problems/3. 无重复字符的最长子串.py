"""
Created at 2023/9/6
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

"""


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:
            return 0

        maxn = 0

        for i in range(len(s)):
            _arr = []
            for j in range(i, len(s)):
                if s[j] not in _arr:
                    _arr.append(s[j])
                else:
                    break
            maxn = max(maxn, len(_arr))

        return maxn

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        left = 0
        lookup = set()

        max_len = 0
        cur_len = 0

        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[i])

                left += 1
                cur_len -= 1

            max_len = max(max_len, cur_len)

            lookup.add(s[i])

        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        哈希表 dic 统计： 指针 j 遍历字符 s ，哈希表统计字符 s[j] 最后一次出现的索引 。
        更新左指针 i ： 根据上轮左指针 i和 dic[s[j]] ，每轮更新左边界 i ，保证区间 [i+1,j]内无重复字符且最大。
        更新结果 res： 取上轮 res 和本轮双指针区间 [i+1,j] 的宽度（即 j−i ）中的最大值。


        :param s:
        :return:
        """
        dic = {}
        res = 0
        i = -1

        for j in range(len(s)):
            if s[j] in dic:
                # 只有在重复时才会移动 i
                i = max(dic[s[j]], i)

            dic[s[j]] = j

            res = max(res, j - i)

        return res


if __name__ == '__main__':
    Solution().lengthOfLongestSubstring('abcxabcbb')
    Solution().lengthOfLongestSubstring('bbbbb')
    Solution().lengthOfLongestSubstring('au')
