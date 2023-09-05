"""
Created at 2023/9/5


"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._inner(root)

    def _inner(self, node: Optional[TreeNode]):
        if not node:
            return 0

        return 1 + max(self._inner(node.left), self._inner(node.right))
