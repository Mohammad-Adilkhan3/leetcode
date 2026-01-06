# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, r: Optional[TreeNode]) -> int:
        z = Counter()
        (f:=lambda n,i:n and (z.update({i:n.val}),f(n.left,i+1),f(n.right,i+1)))(r,1)
        return max(z,key=z.get)
        