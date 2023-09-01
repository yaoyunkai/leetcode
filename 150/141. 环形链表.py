"""


给你一个链表的头节点 head ，判断链表中是否有环。

Created at 2023/9/1
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return f'({self.val} -> {self.next.val})'
        else:
            return f'({self.val} -> null)'


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head
        slow = head

        while fast:
            fast = fast.next

            if fast:
                fast = fast.next

            if fast is slow:
                return True

            slow = slow.next

        return False

    def getKthFromEnd(self, head: Optional[ListNode], k: int):
        """
        先来看"倒数第k个元素的问题"。设有两个指针 p 和 q，初始时均指向头结点。首先，先让 p 沿着 next 移动 k 次。
        此时，p 指向第 k+1个结点，q 指向头节点，两个指针的距离为 k 。
        然后，同时移动 p 和 q，直到 p 指向空，此时 q 即指向倒数第 k 个结点。


        :param head:
        :param k:
        :return:
        """

        # 假设k不会大于链表的长度

        p = head
        q = head

        while k > 0:
            p = p.next
            k -= 1

        while p is not None:
            p = p.next
            q = q.next

        return q

    def getMiddleNode(self, head: Optional[ListNode]):
        """
        设有两个指针 fast 和 slow，初始时指向头节点。每次移动时，fast向后走两次，slow向后走一次，直到 fast 无法向后走两次。
        这使得在每轮移动之后。fast 和 slow 的距离就会增加一。设链表有 n 个元素，那么最多移动 n/2 轮。
        当 n 为奇数时，slow 恰好指向中间结点，当 n 为 偶数时，slow 恰好指向中间两个结点的靠前一个

        :param head:
        :return:
        """

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a6 = ListNode(6)
    a7 = ListNode(7)

    a6.next = a7
    a5.next = a6
    a4.next = a5
    a3.next = a4
    a2.next = a3
    a1.next = a2

    # print(a1)

    # Solution().getKthFromEnd(a1, 3)

    Solution().getMiddleNode(a2)
    Solution().getMiddleNode(a1)
