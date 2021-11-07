# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        ## https://www.youtube.com/watch?v=0K0uCMYq5ng
        
        ## Creating a helper function
        def helper(l, r):
            ## Base case: If the left pointer becomes greater than the right pointer
            if l > r:
                return None
            
            ## Getting the middle index
            m = (l + r) // 2
            
            ## Creating a node with middle element as the root
            root = TreeNode(nums[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            
            return root
        
        return helper(0, len(nums) - 1)
