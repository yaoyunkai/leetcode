# 27. 移除元素

## 题目

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1：

```
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
```

示例 2：

```
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
```

## 解题

### A

先计算出要移除的个数count，获取数组的长度length, 那么新的长度为 length-count 。

然后调用 count次 remove(val).

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        count = 0
        length = len(nums)
        for i in nums:
            if i == val:
                count += 1

        for i in range(count):
            nums.remove(val)

        return length - count
```

### B

先给出一个变量 j =0；

遍历数组，如果元素!=val,那么将元素放到索引为j的位置，然后j++。

最后被移动的元素的个数j即为新数组的长度。

问题：元素被移动的次数会很多。

```python
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        j = 0
        for i, number in enumerate(nums):
            if number != val:
                nums[j] = nums[i]
                j += 1
        return j
```

