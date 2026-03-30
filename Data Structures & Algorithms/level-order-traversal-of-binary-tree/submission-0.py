# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = []
        queue.append(root)

        while queue:
            tempList = []
            valueList = []
            while queue:
                node = queue.pop(0)
                tempList.append(node)
                valueList.append(node.val)
            for item in tempList:
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            result.append(valueList)
        
        return result