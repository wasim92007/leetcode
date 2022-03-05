#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (69.95%)
# Likes:    7080
# Dislikes: 313
# Total Accepted:    1.4M
# Total Submissions: 1.9M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## Inorder traversal is left-root-right
        ## https://www.youtube.com/watch?v=RJhh3Jcc9zw&t=884s
        ##            1
        ##          /   \
        ##         /     \
        ##        2       3
        ##       / \     / \
        ##      /   \   /   \
        ##     4     5 6     7
        ## Algorithm 2: We will use iteration and stack to store the value
        ## Since the stack if LIFO: We will add in reverse oder
        ## Stack = [root, left]
        result = []
        stack = []

        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result


        ## Algorithm 1: We will use the recursion
        ## Base case: When the node is empty
        if root is None:
            return []
        else:
            return self.inorderTraversal(root=root.left) + [root.val] + self.inorderTraversal(root=root.right)
        
# @lc code=end

