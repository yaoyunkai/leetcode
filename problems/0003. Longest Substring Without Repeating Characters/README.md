# 3. 无重复字符的最长子串

## 题目

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

示例 1:

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

示例 2:

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

示例 3:

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

## 解题

### A

变量保存当前最大长度：max_len

两次迭代字符串：

index 从`0`开始，到 `len-1` 停止。

内层的for循环从index开始，到 `len-1` 停止，内层循环时用list保存index到不重复的字符，遇到重复的字符跳出循环。

比较max_len和这一次的长度取较大者。

外层循环结束，即可得出最大长度。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
```

### B 滑动窗口

其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

如何移动？

我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候，求出解！

时间复杂度：O(n)

