from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        _arr = []
        self._run(root, _arr)
        return _arr

    def _run(self, node, array):
        if not node:
            return
        array.append(node.val)
        self._run(node.left, array)
        self._run(node.right, array)
