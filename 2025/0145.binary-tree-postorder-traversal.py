from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        _arr = []
        self._run(root, _arr)
        return _arr

    def _run(self, node, array):
        if not node:
            return
        self._run(node.left, array)
        self._run(node.right, array)
        array.append(node.val)
