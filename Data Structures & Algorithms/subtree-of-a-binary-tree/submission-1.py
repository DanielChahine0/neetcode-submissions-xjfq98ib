# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:    
        if subRoot is None:
            return True
        elif root is None:
            return False
        elif self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)


    def sameTree(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            left = self.sameTree(p.left, q.left)
            right = self.sameTree(p.right, q.right)
            return left and right
        else:
            return False