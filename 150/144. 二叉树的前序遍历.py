"""
Created at 2023/9/5


"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _run(node):
            if not node:
                return
            res.append(node.val)
            _run(node.left)
            _run(node.right)

        _run(root)
        return res
