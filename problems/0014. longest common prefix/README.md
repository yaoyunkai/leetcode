# 14. 最长公共前缀

## 题目

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1：

```
输入：strs = ["flower","flow","flight"]
输出："fl"
```

示例 2：

```
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
```

## 解题

### A: 纵向扫描

![fig2](.assets/14_fig2.png)

纵向扫描时，从前往后遍历所有字符串的每一列，比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀。

```python
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        length, count = len(strs[0]), len(strs)

        # 遍历每一列
        for i in range(length):
            # 当前列的字符
            ch = strs[0][i]

            # 遍历每个字符
            for j in range(1, count):
                if i == len(strs[j]):
                    return strs[0][:i]
                if strs[j][i] != ch:
                    return strs[0][:i]

        return strs[0]

```

### B

