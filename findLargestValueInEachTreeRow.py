# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        from collections import deque
        q, res = deque([root]), []
        while q:
            res.append(max(node.val for node in q))
            q = deque(child for node in q for child in (node.left, node.right) if child)
        return res
