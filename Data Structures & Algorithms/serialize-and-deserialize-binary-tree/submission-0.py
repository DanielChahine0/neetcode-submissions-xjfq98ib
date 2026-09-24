# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        
        def dfs(node):
            if node:
                serialized.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                serialized.append("N")
        
        dfs(root)
        res = ".".join(serialized)
        print(res)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(".")
        self.i = 0

        def dfs():
            if res[self.i]=="N":
                self.i += 1
                return None
            else:
                node = TreeNode(int(res[self.i]))
                self.i+=1
                node.left = dfs()
                node.right = dfs()
                return node

        val = dfs()

        return val
        



