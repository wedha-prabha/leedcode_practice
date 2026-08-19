class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            # Visit node
            result.append(node.val)
            # Traverse right subtree
            inorder(node.right)
            
        inorder(root)
        return result