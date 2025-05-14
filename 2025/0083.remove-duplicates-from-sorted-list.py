"""
83. 删除排序链表中的重复元素

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        if self.next:
            return f'{self.val} -> {self.next.val}'
        else:
            return f'{self.val}'


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head

        while cur:
            if cur.val == prev.val:
                cur = cur.next
                if cur is None:  # 特殊情况, 后面的元素都是一样
                    prev.next = cur
            else:
                prev.next = cur
                prev = cur

        return head


if __name__ == '__main__':
    # [1,1,2,3,3]
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(3)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    Solution().deleteDuplicates(n1)
