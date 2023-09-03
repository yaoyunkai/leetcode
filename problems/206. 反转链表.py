"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


Created at 2023/9/1
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        if self.next:
            return f'({self.val} -> {self.next.val})'
        else:
            return f'({self.val} -> null)'


class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()

        while head:
            new = ListNode(head.val, root.next)
            root.next = new

            head = head.next

        return root.next

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recur(cur, pre):
            # 终止条件
            if not cur:
                return pre

            # 递归后继结点
            res = recur(cur.next, cur)
            cur.next = pre
            return res

        return recur(head, None)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 不用 new 对象

        cur = head
        pre = None

        while cur:
            """
            保存下一个
            将当前的指向上一个
            将上一个 变为 当前的
            移动cur指针
            
            """
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre


if __name__ == '__main__':
    a3 = ListNode(2)
    a2 = ListNode(4)
    a1 = ListNode(3)

    a3.next = a2
    a2.next = a1

    Solution().reverseList2(a3)
