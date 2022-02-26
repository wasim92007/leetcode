# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        ## Solution from - https://www.youtube.com/watch?v=RJhh3Jcc9zw
        result, stack = [], []
        ## Iterative solution
        while root is not None or stack != []:
            ## Travel as long as there is left node
            while root:
                stack.append(root)
                root = root.left
                
            ## Keep on adding to the list
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return result
        
        
        ## Compact solution
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return []
        
        #### My solution
        in_order_list = []
        
        ## If there is a tree
        if root:
            ## Traverse left
            if root.left:
                in_order_list += self.inorderTraversal(root.left)
                
            ## Add root
            in_order_list.append(root.val)
            
            ## Traverse right
            if root.right:
                in_order_list += self.inorderTraversal(root.right)
        
            return in_order_list
        
        ## In case there is no tree
        return root
