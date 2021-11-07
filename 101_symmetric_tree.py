# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## TODO: Do it using iteration
    '''
    #### My code working fine
    ## A function to check if left is reflection of right
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        ## In case both leaf are None return True
        if left is None and right is None:
            return True
        ## If left is None but right is non None return False
        elif left is None and right is not None:
            return False
        ## If left is not None but right is None return False
        elif left is not None and right is None:
            return False
        ## If both are not None but values are not same return False
        elif left.val != right.val:
            return False
        ## Other wise check the below, remember it is a mirror image
        else:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    '''
    
    ## Compact version of the code:
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left and right:
            return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        return left == right
    
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
