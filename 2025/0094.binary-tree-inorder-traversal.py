"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        _arr = []
        self._run(root, _arr)
        return _arr

    def _run(self, node, array):
        if not node:
            return
        self._run(node.left, array)
        array.append(node.val)
        self._run(node.right, array)
