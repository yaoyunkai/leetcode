"""
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例 1：

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明：不存在返回-1。

created at 2025/6/2
"""
from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        try:
            return words.index(s)
        except:
            return -1
